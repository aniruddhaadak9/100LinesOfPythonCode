#!/usr/bin/env python3
"""
Auto Log File Archiver

This script automatically moves log files older than a specified number of days
to an 'archive' folder. It can archive files based on age and optionally by size.

Usage:
    python auto_log_file_archiver.py [--log-dir LOG_DIR] [--days DAYS] [--size SIZE]
"""

import os
import sys
import shutil
import argparse
from datetime import datetime, timedelta
from pathlib import Path


def get_file_age_days(file_path):
    """Calculate the age of a file in days."""
    file_modified_time = os.path.getmtime(file_path)
    file_modified_date = datetime.fromtimestamp(file_modified_time)
    age = datetime.now() - file_modified_date
    return age.days


def get_file_size_mb(file_path):
    """Get file size in megabytes."""
    return os.path.getsize(file_path) / (1024 * 1024)


def should_archive(file_path, days_threshold, size_threshold_mb=None):
    """Determine if a file should be archived based on age and optionally size."""
    age_days = get_file_age_days(file_path)
    
    # Check age threshold
    if age_days < days_threshold:
        return False
    
    # Check size threshold if provided
    if size_threshold_mb is not None:
        file_size_mb = get_file_size_mb(file_path)
        if file_size_mb < size_threshold_mb:
            return False
    
    return True


def archive_log_files(log_dir, days=7, size_mb=None, extensions=None):
    """Archive log files older than specified days to an archive folder."""
    if extensions is None:
        extensions = ['.log', '.txt']
    
    log_path = Path(log_dir)
    
    if not log_path.exists():
        print(f"Error: Log directory '{log_dir}' does not exist.")
        return 0
    
    # Create archive directory if it doesn't exist
    archive_path = log_path / 'archive'
    archive_path.mkdir(exist_ok=True)
    
    archived_count = 0
    total_size_mb = 0
    
    print(f"Scanning log directory: {log_path}")
    print(f"Archiving files older than {days} days...")
    
    # Iterate through files in the log directory
    for file_path in log_path.iterdir():
        # Skip if it's a directory or the archive folder
        if file_path.is_dir():
            continue
        
        # Check file extension
        if file_path.suffix.lower() not in extensions:
            continue
        
        # Check if file should be archived
        if should_archive(file_path, days, size_mb):
            try:
                # Create destination path with date prefix
                file_age = get_file_age_days(file_path)
                dest_name = f"{file_path.stem}_{datetime.now().strftime('%Y%m%d')}{file_path.suffix}"
                dest_path = archive_path / dest_name
                
                # Move file to archive
                shutil.move(str(file_path), str(dest_path))
                
                file_size = get_file_size_mb(file_path) if file_path.exists() else get_file_size_mb(dest_path)
                total_size_mb += file_size
                archived_count += 1
                
                print(f"✓ Archived: {file_path.name} (age: {file_age} days, size: {file_size:.2f} MB)")
            except Exception as e:
                print(f"✗ Error archiving {file_path.name}: {e}")
    
    print(f"\nArchiving complete!")
    print(f"Total files archived: {archived_count}")
    print(f"Total size archived: {total_size_mb:.2f} MB")
    print(f"Archive location: {archive_path}")
    
    return archived_count


def main():
    """Main function to parse arguments and run the archiver."""
    parser = argparse.ArgumentParser(description='Auto Log File Archiver')
    parser.add_argument('--log-dir', type=str, default='./logs',
                        help='Directory containing log files (default: ./logs)')
    parser.add_argument('--days', type=int, default=7,
                        help='Archive files older than this many days (default: 7)')
    parser.add_argument('--size', type=float, default=None,
                        help='Minimum file size in MB to archive (optional)')
    parser.add_argument('--extensions', type=str, default='.log,.txt',
                        help='Comma-separated file extensions to archive (default: .log,.txt)')
    
    args = parser.parse_args()
    
    # Parse extensions
    extensions = [ext.strip() if ext.startswith('.') else f'.{ext.strip()}' 
                  for ext in args.extensions.split(',')]
    
    # Run archiver
    archive_log_files(args.log_dir, args.days, args.size, extensions)


if __name__ == '__main__':
    main()

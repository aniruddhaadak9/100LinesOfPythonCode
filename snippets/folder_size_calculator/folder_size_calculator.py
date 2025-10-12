#!/usr/bin/env python3
"""
Folder Size Calculator

Calculates and displays the size of each folder in a directory in a human-readable format.
Supports recursive scanning and sorting by size.

Author: Comet Assistant
Issue: #786
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple


def get_size(path: str) -> int:
    """Calculate total size of a directory recursively.
    
    Args:
        path: Path to the directory
        
    Returns:
        Total size in bytes
    """
    total = 0
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                try:
                    if entry.is_file(follow_symlinks=False):
                        total += entry.stat(follow_symlinks=False).st_size
                    elif entry.is_dir(follow_symlinks=False):
                        total += get_size(entry.path)
                except (PermissionError, OSError):
                    pass
    except (PermissionError, OSError):
        pass
    return total


def format_size(size: int) -> str:
    """Convert bytes to human-readable format.
    
    Args:
        size: Size in bytes
        
    Returns:
        Formatted size string (e.g., '1.5 GB')
    """
    units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    unit_index = 0
    size_float = float(size)
    
    while size_float >= 1024 and unit_index < len(units) - 1:
        size_float /= 1024
        unit_index += 1
    
    return f"{size_float:.2f} {units[unit_index]}"


def scan_directory(directory: str) -> List[Tuple[str, int]]:
    """Scan directory and get folder sizes.
    
    Args:
        directory: Path to scan
        
    Returns:
        List of tuples (folder_name, size_in_bytes)
    """
    folder_sizes = []
    
    try:
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_dir(follow_symlinks=False):
                    size = get_size(entry.path)
                    folder_sizes.append((entry.name, size))
    except (PermissionError, OSError) as e:
        print(f"Error accessing directory: {e}")
        sys.exit(1)
    
    return folder_sizes


def display_results(folder_sizes: List[Tuple[str, int]], sort_by_size: bool = True):
    """Display folder sizes in a formatted table.
    
    Args:
        folder_sizes: List of (folder_name, size) tuples
        sort_by_size: Whether to sort by size (default: True)
    """
    if not folder_sizes:
        print("No folders found in the directory.")
        return
    
    if sort_by_size:
        folder_sizes.sort(key=lambda x: x[1], reverse=True)
    
    print("\n" + "=" * 70)
    print(f"{'Folder Name':<40} {'Size':>20}")
    print("=" * 70)
    
    total_size = 0
    for name, size in folder_sizes:
        print(f"{name:<40} {format_size(size):>20}")
        total_size += size
    
    print("=" * 70)
    print(f"{'Total':<40} {format_size(total_size):>20}")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    
    if not os.path.exists(target_dir):
        print(f"Error: Directory '{target_dir}' does not exist.")
        sys.exit(1)
    
    if not os.path.isdir(target_dir):
        print(f"Error: '{target_dir}' is not a directory.")
        sys.exit(1)
    
    print(f"Scanning directory: {os.path.abspath(target_dir)}")
    folder_sizes = scan_directory(target_dir)
    display_results(folder_sizes)

# Folder Size Calculator

## Description
A Python script that calculates and displays the size of each folder in a directory in a human-readable format. The tool recursively scans directories, calculates their total sizes, and presents the information in a sorted, easy-to-read table format.

## Features
- **Recursive Calculation**: Accurately calculates the total size of each folder including all subdirectories and files
- **Human-Readable Format**: Displays sizes in appropriate units (B, KB, MB, GB, TB, PB)
- **Sorted Display**: Automatically sorts folders by size (largest first)
- **Error Handling**: Gracefully handles permission errors and inaccessible files
- **Total Size**: Shows the cumulative size of all folders scanned
- **Cross-Platform**: Works on Windows, Linux, and macOS

## Requirements
- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## Usage

### Basic Usage
Scan the current directory:
```bash
python folder_size_calculator.py
```

### Scan a Specific Directory
```bash
python folder_size_calculator.py /path/to/directory
```

### Examples
```bash
# Scan the current directory
python folder_size_calculator.py

# Scan your home directory
python folder_size_calculator.py ~

# Scan a specific folder
python folder_size_calculator.py /var/log
```

## Output Format
```
Scanning directory: /path/to/directory

======================================================================
Folder Name                              Size
======================================================================
large_folder                             15.67 GB
medium_folder                            245.32 MB
small_folder                             1.24 KB
======================================================================
Total                                    15.92 GB
======================================================================
```

## How It Works
1. The script scans the specified directory (or current directory if none specified)
2. For each folder found, it recursively calculates the total size including all subfolders and files
3. Sizes are converted to human-readable format (automatically selecting the most appropriate unit)
4. Results are displayed in a sorted table with the largest folders first
5. A total size summary is shown at the bottom

## Error Handling
The script handles common errors gracefully:
- **Permission Errors**: Skips folders/files that are not accessible
- **Invalid Paths**: Provides clear error messages for non-existent or invalid directories
- **Symbolic Links**: Does not follow symbolic links to avoid circular references

## Contributing
This script was created as part of the [100LinesOfPythonCode](https://github.com/sumanth-0/100LinesOfPythonCode) project.

## License
This project follows the license of the parent repository.

## Issue Reference
Resolves issue #786 - Folder Size Calculator

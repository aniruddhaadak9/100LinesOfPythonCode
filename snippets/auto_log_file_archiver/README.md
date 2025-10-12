# Auto Log File Archiver

## Description

A Python script that automatically moves log files older than a specified number of days to an 'archive' folder. This tool helps keep your log directories organized by archiving old log files based on their age and optionally by size.

## Features

- ✨ **Automatic Archiving**: Automatically moves old log files to an archive folder
- 📅 **Date-based Filtering**: Archive files older than a configurable number of days (default: 7 days)
- 💾 **Size-based Filtering**: Optional minimum file size threshold for archiving
- 📁 **Organized Structure**: Creates an 'archive' subfolder within your log directory
- 🏷️ **Date Stamping**: Adds date stamps to archived files to prevent name conflicts
- 🔍 **File Extension Support**: Configurable file extensions to target (.log, .txt by default)
- 📊 **Detailed Reports**: Displays statistics about archived files (count, total size)

## Installation

1. Clone this repository or download the script
2. Ensure you have Python 3.6 or higher installed
3. No additional dependencies required (uses standard library only)

## Usage

### Basic Usage

```bash
python auto_log_file_archiver.py
```

This will archive log files older than 7 days from the default `./logs` directory.

### Custom Log Directory

```bash
python auto_log_file_archiver.py --log-dir /path/to/logs
```

### Custom Age Threshold

Archive files older than 14 days:

```bash
python auto_log_file_archiver.py --days 14
```

### Size-based Archiving

Archive only files larger than 10 MB:

```bash
python auto_log_file_archiver.py --size 10
```

### Custom File Extensions

```bash
python auto_log_file_archiver.py --extensions .log,.txt,.out
```

### Combined Options

```bash
python auto_log_file_archiver.py --log-dir /var/logs --days 30 --size 5 --extensions .log
```

## Command Line Arguments

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `--log-dir` | string | `./logs` | Directory containing log files |
| `--days` | integer | `7` | Archive files older than this many days |
| `--size` | float | `None` | Minimum file size in MB to archive (optional) |
| `--extensions` | string | `.log,.txt` | Comma-separated file extensions to archive |

## Example Output

```
Scanning log directory: /var/logs
Archiving files older than 7 days...
✓ Archived: app.log (age: 10 days, size: 2.34 MB)
✓ Archived: debug.log (age: 15 days, size: 5.67 MB)
✓ Archived: error.log (age: 8 days, size: 0.89 MB)

Archiving complete!
Total files archived: 3
Total size archived: 8.90 MB
Archive location: /var/logs/archive
```

## How It Works

1. The script scans the specified log directory
2. For each file with a matching extension:
   - Calculates the file's age based on last modification time
   - Checks if the file meets the age threshold
   - Optionally checks if the file meets the size threshold
3. Matching files are moved to an `archive` subfolder
4. Archived files are renamed with a date stamp to prevent conflicts
5. Statistics are displayed showing the archiving results

## Automation with Cron (Linux/macOS)

To run this script automatically every day at midnight:

```bash
0 0 * * * /usr/bin/python3 /path/to/auto_log_file_archiver.py --log-dir /var/logs
```

## Automation with Task Scheduler (Windows)

1. Open Task Scheduler
2. Create a new task
3. Set the trigger to run daily
4. Set the action to run Python with the script path

## Requirements

- Python 3.6 or higher
- No external dependencies

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Related Issue

This script addresses issue #787: Auto Log File Archiver

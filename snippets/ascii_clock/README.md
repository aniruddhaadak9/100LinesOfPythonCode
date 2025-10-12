# ASCII Clock ⏰

A live terminal clock that displays the current time using large ASCII art characters.

## Description

This Python script creates an animated ASCII clock in your terminal that updates every second. The time is displayed using block characters (█) to create large, easy-to-read digits.

## Features

- 🕐 Real-time clock display
- 🎨 Large ASCII art digits
- 🔄 Auto-updating every second
- 💻 Cross-platform (Windows, macOS, Linux)
- 🚪 Clean exit with Ctrl+C

## Requirements

- Python 3.x
- No external dependencies (uses only standard library)

## Installation

No installation required! Just ensure you have Python 3 installed on your system.

## Usage

1. Navigate to the script directory:
```bash
cd snippets/ascii_clock
```

2. Run the script:
```bash
python ascii_clock.py
```

or

```bash
python3 ascii_clock.py
```

3. The clock will start displaying the current time in ASCII art format

4. To exit, press `Ctrl+C`

## Example Output

```
 ██████        ██████    
██    ██        ██    ██  
██    ██  ██  ██    ██  
██    ██        ██    ██  
 ██████    ██   ██████   

Current Time: 14:23:45

Press Ctrl+C to exit
```

## How It Works

The script uses a dictionary to store ASCII art representations of each digit (0-9) and the colon (:). It continuously:
1. Gets the current system time
2. Converts each character to its ASCII art representation
3. Clears the terminal screen
4. Displays the ASCII art time
5. Waits 1 second before updating

## Code Highlights

- **DIGITS Dictionary**: Contains 5-row ASCII art for each digit
- **get_ascii_time()**: Converts time string to ASCII art
- **clear_screen()**: Cross-platform terminal clearing
- **main()**: Main loop with keyboard interrupt handling

## Contributing

This is part of the 100LinesOfPythonCode project. Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests

## Related Issue

References issue #769

## License

This project follows the license of the parent repository.

---

*Created as part of the 100 Lines of Python Code challenge*

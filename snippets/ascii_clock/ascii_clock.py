#!/usr/bin/env python3
"""
ASCII Clock - A live terminal clock with ASCII art display
Displays current time using large ASCII art characters
Press Ctrl+C to exit
"""

import time
import os
import sys

# ASCII art representations of digits (5 rows each)
DIGITS = {
    '0': [
        " ██████  ",
        "██    ██ ",
        "██    ██ ",
        "██    ██ ",
        " ██████  "
    ],
    '1': [
        "   ██    ",
        " ████    ",
        "   ██    ",
        "   ██    ",
        "████████ "
    ],
    '2': [
        " ██████  ",
        "      ██ ",
        " ██████  ",
        "██       ",
        "████████ "
    ],
    '3': [
        " ██████  ",
        "      ██ ",
        " ██████  ",
        "      ██ ",
        " ██████  "
    ],
    '4': [
        "██    ██ ",
        "██    ██ ",
        "████████ ",
        "      ██ ",
        "      ██ "
    ],
    '5': [
        "████████ ",
        "██       ",
        "███████  ",
        "      ██ ",
        "███████  "
    ],
    '6': [
        " ██████  ",
        "██       ",
        "███████  ",
        "██    ██ ",
        " ██████  "
    ],
    '7': [
        "████████ ",
        "      ██ ",
        "    ██   ",
        "  ██     ",
        "  ██     "
    ],
    '8': [
        " ██████  ",
        "██    ██ ",
        " ██████  ",
        "██    ██ ",
        " ██████  "
    ],
    '9': [
        " ██████  ",
        "██    ██ ",
        " ███████ ",
        "      ██ ",
        " ██████  "
    ],
    ':': [
        "         ",
        "   ██    ",
        "         ",
        "   ██    ",
        "         "
    ]
}

def get_ascii_time(time_str):
    """Convert time string to ASCII art representation"""
    lines = ['', '', '', '', '']
    for char in time_str:
        for i in range(5):
            lines[i] += DIGITS[char][i] + ' '
    return '\n'.join(lines)

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """Main loop - continuously display the current time"""
    try:
        while True:
            # Get current time in HH:MM:SS format
            current_time = time.strftime("%H:%M:%S")
            
            # Clear screen and display ASCII clock
            clear_screen()
            print("\n" * 2)
            print(get_ascii_time(current_time))
            print("\n" * 2)
            print(f"Current Time: {current_time}")
            print("\nPress Ctrl+C to exit")
            
            # Wait 1 second before updating
            time.sleep(1)
            
    except KeyboardInterrupt:
        clear_screen()
        print("\nASCII Clock stopped. Goodbye!")
        sys.exit(0)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Random Flag Creator

Generates random flag patterns with various layouts, colors, and designs.
Creates visual flag representations using colored blocks.

Issue: #766
"""

import random
from typing import List, Tuple

# ANSI color codes for terminal output
COLORS = {
    'red': '\033[41m',
    'blue': '\033[44m',
    'green': '\033[42m',
    'yellow': '\033[43m',
    'white': '\033[47m',
    'black': '\033[40m',
    'magenta': '\033[45m',
    'cyan': '\033[46m',
    'reset': '\033[0m'
}

def get_random_colors(n: int) -> List[str]:
    """Select n random colors from available colors."""
    available = [k for k in COLORS.keys() if k != 'reset']
    return random.sample(available, min(n, len(available)))

def create_horizontal_stripes(width: int = 30, height: int = 12) -> str:
    """Create a flag with horizontal stripes."""
    colors = get_random_colors(random.randint(2, 4))
    stripe_height = height // len(colors)
    flag = []
    
    for i, color in enumerate(colors):
        for _ in range(stripe_height):
            flag.append(COLORS[color] + ' ' * width + COLORS['reset'])
    
    return '\n'.join(flag)

def create_vertical_stripes(width: int = 30, height: int = 12) -> str:
    """Create a flag with vertical stripes."""
    colors = get_random_colors(random.randint(2, 4))
    stripe_width = width // len(colors)
    flag = []
    
    for _ in range(height):
        row = ''
        for color in colors:
            row += COLORS[color] + ' ' * stripe_width + COLORS['reset']
        flag.append(row)
    
    return '\n'.join(flag)

def create_checker_pattern(width: int = 30, height: int = 12) -> str:
    """Create a flag with checker pattern."""
    colors = get_random_colors(2)
    block_size = 3
    flag = []
    
    for row in range(height):
        line = ''
        for col in range(width):
            color_idx = ((row // block_size) + (col // block_size)) % 2
            line += COLORS[colors[color_idx]] + ' ' + COLORS['reset']
        flag.append(line)
    
    return '\n'.join(flag)

def create_bordered_flag(width: int = 30, height: int = 12) -> str:
    """Create a flag with a border and center."""
    colors = get_random_colors(2)
    border_color, center_color = colors[0], colors[1]
    flag = []
    
    for row in range(height):
        line = ''
        for col in range(width):
            if row < 2 or row >= height - 2 or col < 2 or col >= width - 2:
                line += COLORS[border_color] + ' ' + COLORS['reset']
            else:
                line += COLORS[center_color] + ' ' + COLORS['reset']
        flag.append(line)
    
    return '\n'.join(flag)

def main():
    """Generate and display a random flag."""
    patterns = [
        ('Horizontal Stripes', create_horizontal_stripes),
        ('Vertical Stripes', create_vertical_stripes),
        ('Checker Pattern', create_checker_pattern),
        ('Bordered Flag', create_bordered_flag)
    ]
    
    print("\n=== Random Flag Creator ===")
    print("\nGenerating a random flag pattern...\n")
    
    pattern_name, pattern_func = random.choice(patterns)
    print(f"Pattern: {pattern_name}\n")
    print(pattern_func())
    print("\n" + "=" * 32)

if __name__ == '__main__':
    main()

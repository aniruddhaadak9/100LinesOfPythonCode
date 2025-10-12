# Random Flag Creator 🏴

**Issue:** #766

## Overview

A Python script that generates random flag patterns using ANSI colors in the terminal. The script creates visual flag representations with various layouts, colors, and designs.

## Features

- 🎨 **Multiple Pattern Types**:
  - Horizontal Stripes
  - Vertical Stripes
  - Checker Pattern
  - Bordered Flag

- 🌈 **Colorful Output**: Uses ANSI color codes to display flags in terminal with 8 different colors:
  - Red, Blue, Green, Yellow, White, Black, Magenta, Cyan

- 🎲 **Randomization**: Each run generates a random pattern with random color combinations

## Requirements

- Python 3.x
- Terminal with ANSI color support (most modern terminals)

## Usage

### Basic Usage

```bash
python random_flag_creator.py
```

### Example Output

```
=== Random Flag Creator ===

Generating a random flag pattern...

Pattern: Horizontal Stripes

[Colorful flag pattern displayed here]

================================
```

## How It Works

1. **Pattern Selection**: Randomly selects one of four pattern types
2. **Color Selection**: Randomly picks 2-4 colors from the available palette
3. **Flag Generation**: Creates a flag using the selected pattern and colors
4. **Display**: Outputs the flag pattern to the terminal using ANSI colors

## Pattern Details

### Horizontal Stripes
Creates 2-4 horizontal colored stripes across the flag.

### Vertical Stripes
Creates 2-4 vertical colored stripes down the flag.

### Checker Pattern
Creates an alternating checkerboard pattern with 2 colors.

### Bordered Flag
Creates a flag with a colored border and a different colored center.

## Code Structure

- `get_random_colors(n)`: Selects n random colors from the palette
- `create_horizontal_stripes()`: Generates horizontal stripe pattern
- `create_vertical_stripes()`: Generates vertical stripe pattern
- `create_checker_pattern()`: Generates checkerboard pattern
- `create_bordered_flag()`: Generates bordered flag pattern
- `main()`: Main function that orchestrates flag generation and display

## Contributing

Contributions are welcome! Feel free to:
- Add new pattern types
- Enhance color combinations
- Improve flag generation algorithms
- Add customization options

## License

This project is part of the 100 Lines of Python Code repository.

---

**Created for Issue #766: Random Flag Creator**

# Comic Strip Quote Generator

## Description

A fun Python script that overlays random funny quotes on cartoon images, perfect for creating memes or entertaining content!

## Features

- Randomly selects from a collection of 15 funny quotes
- Automatically adjusts font size based on image dimensions
- Implements word wrapping for longer quotes
- Adds text outline for better readability
- Cross-platform font support (Windows, macOS, Linux)

## Requirements

- Python 3.6+
- Pillow (PIL) library

## Installation

```bash
pip install Pillow
```

## Usage

```bash
python comic_strip_quote_generator.py <input_image_path> [output_image_path]
```

### Examples

```bash
# Create output with default name (output_with_quote.png)
python comic_strip_quote_generator.py cartoon.jpg

# Specify custom output filename
python comic_strip_quote_generator.py cartoon.jpg funny_meme.png
```

## How it Works

1. Opens the specified cartoon image
2. Randomly selects a funny quote from the predefined list
3. Calculates optimal font size based on image width
4. Wraps text to fit within 90% of image width
5. Positions text at the bottom center of the image
6. Adds black outline for contrast
7. Overlays white text on top
8. Saves the result

## Sample Quotes

The generator includes quotes like:
- "I'm not lazy, I'm on energy-saving mode."
- "My bed is a magical place where I suddenly remember everything I forgot to do."
- "WiFi went down for five minutes, so I had to talk to my family."
- And many more!

## Customization

You can easily customize the script by:
- Adding your own quotes to the `FUNNY_QUOTES` list
- Modifying text color, outline thickness, or positioning
- Changing the font size calculation formula

## Contributing

Feel free to submit pull requests with:
- New funny quotes
- Feature enhancements
- Bug fixes
- Improved font handling

## License

This project is part of the 100 Lines of Python Code collection.

## Related Issues

This implements [Issue #767](https://github.com/sumanth-0/100LinesOfPythonCode/issues/767) - Comic Strip Quote Generator

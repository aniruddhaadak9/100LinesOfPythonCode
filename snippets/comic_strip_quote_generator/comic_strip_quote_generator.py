#!/usr/bin/env python3
"""
Comic Strip Quote Generator
Overlays random funny quotes on cartoon images.
"""

import random
from PIL import Image, ImageDraw, ImageFont
import os
import sys

# Collection of funny quotes
FUNNY_QUOTES = [
    "I'm not lazy, I'm on energy-saving mode.",
    "My bed is a magical place where I suddenly remember everything I forgot to do.",
    "I'm not arguing, I'm just explaining why I'm right.",
    "I don't need anger management. I need people to stop making me angry.",
    "Why fall in love when you can fall asleep?",
    "I followed my heart. It led me to the fridge.",
    "Exercise? I thought you said extra fries!",
    "I'm on a seafood diet. I see food and I eat it.",
    "WiFi went down for five minutes, so I had to talk to my family.",
    "I'm not short, I'm concentrated awesome!",
    "Common sense is like deodorant. Those who need it most never use it.",
    "I put my phone in airplane mode, but it's still not flying.",
    "Life is short. Smile while you still have teeth.",
    "I don't have a bad handwriting, I have my own font.",
    "The early bird can have the worm. I'll have coffee instead."
]

def get_font(size=40):
    """Get a font object, trying multiple fallback options."""
    font_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "C:\\Windows\\Fonts\\arial.ttf",
    ]
    
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except:
                pass
    return ImageFont.load_default()

def add_text_to_image(image_path, output_path, quote=None):
    """Add a random quote to an image."""
    if quote is None:
        quote = random.choice(FUNNY_QUOTES)
    
    # Open the image
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    
    # Get image dimensions
    width, height = img.size
    
    # Calculate font size based on image width
    font_size = max(20, int(width / 20))
    font = get_font(font_size)
    
    # Word wrap the quote
    words = quote.split()
    lines = []
    current_line = []
    
    for word in words:
        current_line.append(word)
        test_line = ' '.join(current_line)
        bbox = draw.textbbox((0, 0), test_line, font=font)
        if bbox[2] - bbox[0] > width * 0.9:
            current_line.pop()
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]
    if current_line:
        lines.append(' '.join(current_line))
    
    # Calculate text position (bottom center)
    text_height = len(lines) * (font_size + 10)
    y_position = height - text_height - 20
    
    # Draw text with outline for better visibility
    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        x_position = (width - text_width) // 2
        y = y_position + i * (font_size + 10)
        
        # Draw outline (black)
        for offset_x in [-2, 0, 2]:
            for offset_y in [-2, 0, 2]:
                draw.text((x_position + offset_x, y + offset_y), line, 
                         font=font, fill='black')
        # Draw text (white)
        draw.text((x_position, y), line, font=font, fill='white')
    
    # Save the image
    img.save(output_path)
    return output_path

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python comic_strip_quote_generator.py <image_path> [output_path]")
        sys.exit(1)
    
    input_image = sys.argv[1]
    output_image = sys.argv[2] if len(sys.argv) > 2 else "output_with_quote.png"
    
    if not os.path.exists(input_image):
        print(f"Error: Image file '{input_image}' not found.")
        sys.exit(1)
    
    print(f"Adding quote to {input_image}...")
    result = add_text_to_image(input_image, output_image)
    print(f"Success! Output saved to {result}")

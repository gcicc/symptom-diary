#!/usr/bin/env python3
"""Generate PWA icons for Symptom Diary."""

from PIL import Image, ImageDraw
import os

def create_icon(size):
    """Create an icon with health cross/heart visual."""
    # Create image with dark background
    img = Image.new('RGBA', (size, size), '#0d1117')
    draw = ImageDraw.Draw(img)

    # Create a health cross/heart design in sand color
    margin = int(size * 0.15)
    inner_size = size - (margin * 2)

    # Draw background circle
    circle_color = '#c4a882'
    draw.ellipse(
        [(margin, margin), (margin + inner_size, margin + inner_size)],
        fill=circle_color,
        outline=circle_color
    )

    # Draw a health cross in the center
    cross_width = int(size * 0.08)
    cross_length = int(size * 0.4)
    center_x = size // 2
    center_y = size // 2
    dark_color = '#0d1117'

    # Vertical bar
    draw.rectangle(
        [center_x - cross_width // 2, center_y - cross_length // 2,
         center_x + cross_width // 2, center_y + cross_length // 2],
        fill=dark_color
    )

    # Horizontal bar
    draw.rectangle(
        [center_x - cross_length // 2, center_y - cross_width // 2,
         center_x + cross_length // 2, center_y + cross_width // 2],
        fill=dark_color
    )

    return img

def main():
    """Generate icons for all required sizes."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    sizes = [180, 192, 512]

    for size in sizes:
        icon = create_icon(size)
        filename = f'icon-{size}.png'
        icon.save(filename)
        print(f'Generated {filename}')

if __name__ == '__main__':
    main()

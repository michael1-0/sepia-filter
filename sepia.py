import argparse
from PIL import Image
import sys
import os


def apply_sepia(input_path, output_path, intensity=1.0):
    try:
        image = Image.open(input_path).convert("RGB")
    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error opening image: {e}")
        sys.exit(1)

    width, height = image.size
    pixels = image.load()

    for py in range(height):
        for px in range(width):
            r, g, b = pixels[px, py]

            tr = int(
                (0.393 * r + 0.769 * g + 0.189 * b) * intensity + r * (1 - intensity)
            )
            tg = int(
                (0.349 * r + 0.686 * g + 0.168 * b) * intensity + g * (1 - intensity)
            )
            tb = int(
                (0.272 * r + 0.534 * g + 0.131 * b) * intensity + b * (1 - intensity)
            )

            pixels[px, py] = (min(tr, 255), min(tg, 255), min(tb, 255))

    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    image.save(output_path)
    print(f"Sepia image saved to {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Apply a sepia filter to an image.")
    parser.add_argument("input", help="Path to the input image")
    parser.add_argument("output", help="Path to save the sepia image")
    parser.add_argument(
        "-i",
        "--intensity",
        type=float,
        default=1.0,
        help="Sepia intensity (0.0 to 1.0, default=1.0)",
    )

    args = parser.parse_args()

    if not (0.0 <= args.intensity <= 1.0):
        print("Intensity must be between 0.0 and 1.0")
        sys.exit(1)

    apply_sepia(args.input, args.output, args.intensity)

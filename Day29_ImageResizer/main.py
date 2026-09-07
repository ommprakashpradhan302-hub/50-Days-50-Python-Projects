import os
from PIL import Image

def resize_image(input_path, output_path, width, height):
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Resize the image
            resized_img = img.resize((width, height), Image.LANCZOS)
            # Save the resized image
            resized_img.save(output_path)
            print("✅ Image resized and saved successfully!")
    except FileNotFoundError:
        print("❌ Error: Input image not found!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    input_path = input("Enter the path of the input image: ").strip()
    output_path = input("Enter the path for the resized image: ").strip()
    try:
        width = int(input("Enter new width (in pixels): "))
        height = int(input("Enter new height (in pixels): "))
        if width <= 0 or height <= 0:
            print("❌ Width and height must be positive numbers!")
        else:
            resize_image(input_path, output_path, width, height)
    except ValueError:
        print("❌ Invalid input! Please enter numeric values for width and height.")

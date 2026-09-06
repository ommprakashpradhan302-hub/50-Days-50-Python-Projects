import os
from PIL import Image

def images_to_pdf(image_folder, output_pdf):
    images = []
    # Collect only JPG, JPEG, PNG files
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    if not image_files:
        print("❌ No image files found in the folder!")
        return

    # Sort files to maintain order
    image_files.sort()

    try:
        for file in image_files:
            img_path = os.path.join(image_folder, file)
            img = Image.open(img_path).convert('RGB')  # Ensure RGB mode
            images.append(img)

        # Save all images as a single PDF
        images[0].save(output_pdf, save_all=True, append_images=images[1:])
        print(f"✅ PDF created successfully: {output_pdf}")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        for img in images:
            img.close()  # Close opened images

if __name__ == "__main__":
    folder = input("Enter the path of image folder: ").strip()
    output = input("Enter output PDF file name (e.g., output.pdf): ").strip()
    images_to_pdf(folder, output)

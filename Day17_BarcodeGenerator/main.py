# Barcode Generator
import barcode
from barcode.writer import ImageWriter

def generate_barcode(data, filename):
    # Create barcode object (Code128 is a common barcode format)
    CODE_CLASS = barcode.get_barcode_class('code128')
    barcode_obj = CODE_CLASS(data, writer=ImageWriter())

    # Define the output file path
    filepath = f"{filename}.png"

    # Save the barcode image
    barcode_obj.save(filepath)
    return filepath

def main():
    print("🔖 BARCODE GENERATOR 🔖")
    data = input("👉 Enter text or number: ").strip()
    if not data:
        print("⚠️ Input cannot be empty!")
        return

    filename = input("💾 Enter filename to save (e.g., barcode): ").strip()
    if not filename:
        print("⚠️ Filename cannot be empty!")
        return

    try:
        result = generate_barcode(data, filename)
        print(f"✅ Barcode successfully saved as '{result}'")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")

if __name__ == "__main__":
    main()

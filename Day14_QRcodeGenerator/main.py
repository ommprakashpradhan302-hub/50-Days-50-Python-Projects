import qrcode

def generate_qr(data, filename):
    """Generates a QR code from given data and saves it as an image file."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    # Add data to QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create image from QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save image
    img.save(filename)
    print(f"✅ QR Code successfully saved as '{filename}'")

def main():
    print("🔳 QR CODE GENERATOR 🔳")
    data = input("👉 Enter text or URL: ").strip()
    filename = input("💾 Enter filename to save (e.g., qr.png): ").strip()
    generate_qr(data, filename)

if __name__ == "__main__":
    main()

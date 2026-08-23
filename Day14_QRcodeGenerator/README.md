# 📱 Day 14 - QR Code Generator

A simple Python QR Code Generator that allows the user to enter text or a URL and generate a QR code image that can be saved to the computer.

## 🎯 Objective

To create a QR Code Generator that allows users to:
- Enter text or a URL
- Generate a QR code
- Save the QR code as an image file

## 🛠️ Concepts Used

- User Input
- QR Code Generation
- External Libraries
- File Handling
- Output Display
- Functions

## 📚 Required Libraries

This project uses the following third-party libraries:

- `qrcode`
- `Pillow`

Install them using:

```bash
pip install qrcode[pil]
```

## ⚙️ How It Works

1. The program asks the user to enter text or a URL.
2. The user provides a filename for the QR code image.
3. A QR code is created using the `qrcode` library.
4. The entered data is added to the QR code.
5. The QR code is generated as an image.
6. The image is saved using the filename provided by the user.
7. A success message is displayed.

## ▶️ How to Run

```bash
python main.py
```

## 💻 Example Output

```text
📱 QR CODE GENERATOR 📱

Enter text or URL: https://www.python.org
Enter filename to save (e.g., qr.png): python_qr.png

✅ QR Code successfully saved as 'python_qr.png'
```

## 🧠 What I Learned

- Generating QR codes using Python
- Working with third-party libraries
- Taking and processing user input
- Creating and saving image files
- Using functions to organize code
- Building a practical utility application

## 📁 Project Structure

```text
Day14_QRCodeGenerator/
│
├── main.py
├── README.md
└── requirements.txt
```

## 🚀 50 Days 50 Python Mini Projects
## 👨‍💻 Author

**Omm Prakash Pradhan**
B.Tech AI & ML Student

**Day 14/50** — Learn • Build • Improve

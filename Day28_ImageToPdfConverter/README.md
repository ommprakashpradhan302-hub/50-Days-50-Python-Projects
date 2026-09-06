# 🖼️ Day 28 - Image to PDF Converter

A Python program that converts multiple images from a folder into a single PDF file.

## 🎯 Objective

To create an Image to PDF Converter that merges one or more images into a single PDF document.

## 🛠️ Concepts Used

- File Handling
- Lists
- Loops
- Conditional Statements
- Exception Handling
- User Input
- OS Module
- Pillow (PIL) Library

## 📚 Required Libraries

This project uses the third‑party `Pillow` library.  

Install it using:

```bash
pip install pillow
```

## ⚙️ How It Works

1. The user enters the folder path containing images.
2. The program scans the folder for supported image formats (`.jpg`, `.jpeg`, `.png`).
3. Files are sorted to maintain order.
4. Each image is opened and converted to RGB mode.
5. All images are merged into a single PDF file.
6. The PDF is saved with the user‑specified name.
7. Errors (e.g., no images found) are handled gracefully.

## 💻 Example Output

```text
Enter the path of image folder: C:\MyImages
Enter output PDF file name (e.g., output.pdf): my_images.pdf

✅ PDF created successfully: my_images.pdf
```

*Images are combined into a single PDF file in the order they appear.*

## 🧠 What I Learned

- Working with images using Pillow
- Converting multiple images into a single PDF
- Handling file paths and directories
- Using exception handling for robust programs
- Building a practical real‑world utility

## ▶️ How to Run

```bash
python main.py
```

Make sure the folder contains valid image files and Pillow is installed.

## 📁 Project Structure

```text
Day28_ImageToPDFConverter/
│
├── main.py
└── README.md
```
#🚀 50 Days 50 Python Mini Projects
## 👨‍💻 Author

**Omm Prakash Pradhan**
B.Tech AI & ML Student

**Day 28/50** — Learn • Build • Improve
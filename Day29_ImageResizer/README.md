# 🖼️ Day 29 - Image Resizer

A Python program that resizes an image to a specified width and height while maintaining quality.

## 🎯 Objective

To create an Image Resizer that allows users to adjust image dimensions easily while preserving quality.

## 🛠️ Concepts Used

- File Handling
- Functions
- Exception Handling
- User Input
- Pillow (PIL) Library

## 📚 Required Libraries

This project uses the third‑party `Pillow` library.  

Install it using:

```bash
pip install pillow
```

## ⚙️ How It Works

1. The user enters the path of the input image.
2. The user specifies the output path for the resized image.
3. The user provides new width and height values in pixels.
4. The program opens the image using Pillow.
5. The image is resized using the `Image.LANCZOS` filter for high quality.
6. The resized image is saved to the specified output path.
7. Errors (e.g., invalid file path or non‑numeric input) are handled gracefully.

## 💻 Example Output

```text
Enter the path of the input image: C:\Images\photo.jpg
Enter the path for the resized image: C:\Images\photo_resized.jpg
Enter new width (in pixels): 800
Enter new height (in pixels): 600
✅ Image resized and saved successfully!
```

*The image is resized to the specified dimensions while maintaining quality.*

## 🧠 What I Learned

- Opening and processing images with Pillow
- Resizing images with custom dimensions
- Using filters like `Image.LANCZOS` for better quality
- Handling exceptions for invalid inputs
- Building a practical utility for image management

## ▶️ How to Run

```bash
python main.py
```

Make sure the input image exists and Pillow is installed.

## 📁 Project Structure

```text
Day29_ImageResizer/
│
├── main.py
└── README.md
```
#🚀 50 Days 50 Python Mini Projects
## 👨‍💻 Author

**Omm Prakash Pradhan**
B.Tech AI & ML Student

**Day 29/50** — Learn • Build • Improve
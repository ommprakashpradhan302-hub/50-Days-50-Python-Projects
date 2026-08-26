# Day 17 - Barcode Generator 📊

## 📌 Project Overview

A simple **Barcode Generator** built with Python that converts text or numbers into a barcode image and saves it to the computer.

## 🎯 Objective

To create a program that accepts text or a number from the user, generates a **Code 128 barcode**, and saves it as a PNG image.

## 🧠 Concepts Used

- User Input
- Barcode Generation
- External Libraries
- File Handling
- Output Display
- Error Handling

## 🛠️ Requirements

- Python 3.x
- `python-barcode`
- `Pillow`

### Install Required Libraries

```bash
pip install python-barcode pillow
```

## ⚙️ How It Works

1. The program asks the user to enter text or a number.
2. The user provides a filename for the barcode image.
3. A Code 128 barcode is generated using the `python-barcode` library.
4. The barcode is saved as a PNG image.
5. A success message displays the saved filename.
6. Empty inputs and errors are handled with appropriate messages.

## ▶️ How to Run

```bash
python barcode_generator.py
```

## 💻 Example Output

```text
🔗 BARCODE GENERATOR 🔗

Enter text or number: 1234567890
Enter filename to save (e.g., barcode): my_barcode

✅ Barcode successfully saved as 'my_barcode.png'
```

The generated barcode will be saved as a PNG image.

## 📚 What I Learned

- How to generate barcodes using Python
- How to work with third-party libraries
- How to take and validate user input
- How to save generated images to files
- How to handle errors using `try-except`
- How to build a practical utility application

## 📁 Project Structure

```text
Day-17/
│
├── barcode_generator.py
├── my_barcode.png
└── README.md
```

# 🚀 50 Days 50 Python Mini Projects
## 👨‍💻 Author

**Omm Prakash Pradhan**
B.Tech AI & ML Student

**Day 17/50** — Learn • Build • Improve

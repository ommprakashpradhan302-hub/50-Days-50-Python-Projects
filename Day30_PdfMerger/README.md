# 📚 Day 30 - PDF Merger

A Python program that merges multiple PDF files from a folder into a single PDF file.

## 🎯 Objective

To create a PDF Merger that combines two or more PDF files from a folder into one single PDF document.

## 🛠️ Concepts Used

- File Handling  
- Lists  
- Loops  
- Conditional Statements  
- Exception Handling  
- OS Module  
- PyPDF2 Library  
- User Input

## 📚 Required Libraries

This project uses the third‑party `PyPDF2` library.  

Install it using:

```bash
pip install PyPDF2
```

## ⚙️ How It Works

1. The user enters the folder path containing PDF files.  
2. The program scans the folder for `.pdf` files.  
3. Files are sorted to maintain order.  
4. Each PDF file is appended to a `PdfMerger` object.  
5. All PDFs are merged into a single output file.  
6. The merged PDF is saved with the user‑specified name.  
7. Errors (e.g., missing files or invalid paths) are handled gracefully.

## 💻 Example Output

```text
Enter the path of PDF folder: C:\PDFs
Enter output PDF file name (e.g., merged.pdf): all_pdfs.pdf
✅ PDF merged successfully: all_pdfs.pdf
```

*All PDF files in the folder are combined into one document.*

## 🧠 What I Learned

- Reading and merging PDF files using PyPDF2  
- Handling file paths and directories  
- Sorting files for consistent merging order  
- Managing exceptions for robust code  
- Building a practical file management utility

## ▶️ How to Run

```bash
python main.py
```

Make sure the folder contains valid PDF files and PyPDF2 is installed.

## 📁 Project Structure

```text
Day30_PDFMerger/
│
├── main.py
└── README.md
```
#🚀 50 Days 50 Python Mini Projects
## 👨‍💻 Author

**Omm Prakash Pradhan**
B.Tech AI & ML Student

**Day 30/50** — Learn • Build • Improve
# ✂️ Day 31 - PDF Splitter

A Python program that splits a PDF file into multiple smaller PDF files based on the number of pages specified by the user.

## 🎯 Objective

To create a PDF Splitter that divides a large PDF into smaller parts for easier sharing, organization, or printing.

## 🛠️ Concepts Used

- File Handling  
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

1. The user enters the input PDF file path.  
2. The user specifies the output folder path.  
3. The user provides the number of pages per split file.  
4. The program reads the PDF using `PdfReader`.  
5. It creates new PDF files, each containing the specified number of pages.  
6. The split files are saved in the output folder.  
7. A success message is displayed after all files are created.

## 💻 Example Output

```text
Enter the input PDF file path: C:\PDFs\book.pdf
Enter the output folder path: C:\PDFs\splitted
Enter number of pages per file: 3
✅ Created: C:\PDFs\splitted\split_1.pdf (Pages 1-3)
✅ Created: C:\PDFs\splitted\split_2.pdf (Pages 4-6)
✅ Created: C:\PDFs\splitted\split_3.pdf (Pages 7-9)
✅ Created: C:\PDFs\splitted\split_4.pdf (Pages 10)
✅ Total 4 PDF file(s) created successfully!
```

*Each split file contains the specified number of pages.*

## 🧠 What I Learned

- Reading and writing PDF files using PyPDF2  
- Splitting large PDFs into smaller parts  
- Handling file paths and directories  
- Managing exceptions for robust code  
- Building a practical file management utility

## ▶️ How to Run

```bash
python main.py
```

Make sure the input PDF file exists and PyPDF2 is installed.

## 📁 Project Structure

```text
Day31_PDFSplitter/
│
├── main.py
└── README.md
```
#🚀 50 Days 50 Python Mini Projects
## 👨‍💻 Author

**Omm Prakash Pradhan**
B.Tech AI & ML Student

**Day 31/50** — Learn • Build • Improve

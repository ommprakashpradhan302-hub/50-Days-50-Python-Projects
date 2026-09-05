# 📝 Day 27 - File Renamer

A Python program that renames multiple files in a folder using a custom naming pattern.

## 🎯 Objective

To create a File Renamer that helps users rename files systematically with a chosen base name and numbering.

## 🛠️ Concepts Used

- Loops
- Conditional Statements
- File Handling
- OS Module
- Functions
- User Input

## 📚 Required Libraries

This project uses Python’s built‑in library:

- `os`

No external libraries are required.

## ⚙️ How It Works

1. The user enters the folder path containing files.
2. The program checks if the folder exists.
3. All files in the folder are listed and sorted.
4. Each file is renamed using the new base name followed by a number.
   - Example: `MyFile_1.png`, `MyFile_2.jpg`, `MyFile_3.txt`
5. The renaming process continues until all files are updated.
6. A success message is displayed at the end.

## 💻 Example Output

```text
Enter the folder path: C:\MyFiles
Enter new base name (e.g., file): MyFile

Renamed: image.png -> MyFile_1.png
Renamed: photo.jpg -> MyFile_2.jpg
Renamed: doc.txt -> MyFile_3.txt
Renamed: notes.pdf -> MyFile_4.pdf

✅ All files renamed successfully!
```

*This program only renames files in the selected folder and does not affect files in subfolders.*

## 🧠 What I Learned

- Listing and sorting files with `os.listdir()`
- Splitting file names and extensions with `os.path.splitext()`
- Renaming files using `os.rename()`
- Handling user input and errors
- Automating repetitive file management tasks

## ▶️ How to Run

```bash
python main.py
```

Make sure the folder path you provide exists and contains files to rename.

## 📁 Project Structure

```text
Day27_FileRenamer/
│
├── main.py
└── README.md
```
#🚀 50 Days 50 Python Mini Projects
## 👨‍💻 Author

**Omm Prakash Pradhan**
B.Tech AI & ML Student

**Day 27/50** — Learn • Build • Improve
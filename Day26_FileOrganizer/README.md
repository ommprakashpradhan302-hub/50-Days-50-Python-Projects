# 🗂️ Day 26 - File Organizer

A Python program that organizes files in a given folder into subfolders based on their file extensions.

## 🎯 Objective

To create a File Organizer that automatically sorts files into categories such as Images, Documents, Videos, Music, Archives, and Others.

## 🛠️ Concepts Used

- Dictionaries
- Loops
- Conditional Statements
- File Handling
- OS Module
- Shutil Module
- User Input
- Functions

## 📚 Required Libraries

This project uses Python’s built‑in libraries:

- `os`
- `shutil`

No external libraries are required.

## ⚙️ How It Works

1. The user enters the folder path to organize.
2. The program checks if the folder exists.
3. Subfolders are created for categories (Images, Documents, Videos, Music, Archives, Others).
4. Files are scanned and moved into the appropriate subfolder based on their extension.
5. Files with unknown extensions are moved to the **Others** folder.
6. The folder structure is updated automatically.

## 💻 Example Output

```text
Enter the folder path to organize: C:\MyFiles
Files organized successfully!
Folder structure:
MyFiles/
 ├── Images/
 │   ├── photo1.jpg
 │   ├── image.png
 ├── Documents/
 │   ├── report.pdf
 │   ├── notes.txt
 ├── Videos/
 │   ├── movie.mp4
 ├── Music/
 │   ├── song.mp3
 ├── Archives/
 │   ├── backup.zip
 ├── Others/
 │   ├── file.xyz
```

*This program only organizes files in the selected folder and does not affect files in subfolders.*

## 🧠 What I Learned

- Using dictionaries to map file extensions
- Creating and managing folders with `os.makedirs`
- Moving files with `shutil.move`
- Handling user input and errors
- Automating file organization tasks
- Building a practical utility for file management

## ▶️ How to Run

```bash
python main.py
```

Make sure the folder path you provide exists and contains files to organize.

## 📁 Project Structure

```text
Day26_FileOrganizer/
│
├── main.py
└── README.md
```
#🚀 50 Days 50 Python Mini Projects
## 👨‍💻 Author

**Omm Prakash Pradhan**
B.Tech AI & ML Student

**Day 26/50** — Learn • Build • Improve
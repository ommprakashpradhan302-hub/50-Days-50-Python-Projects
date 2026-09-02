# 🔠 Day 24 - Word Counter

A Python program that counts words, characters, lines, and sentences in a given text, either entered manually or read from a file.

## 🎯 Objective

To create a Word Counter that helps analyze text by calculating word count, character count, line count, and sentence count.

## 🛠️ Concepts Used

- String Manipulation
- Loops
- Functions
- Regular Expressions
- File Handling
- User Input
- Conditional Statements

## 📚 Required Libraries

This project uses Python’s built‑in libraries.  
No external libraries are required.

## ⚙️ How It Works

1. The user chooses whether to enter text manually or read from a file.
2. If manual input is selected, the user types text until entering `END`.
3. If file input is selected, the program reads the content of the specified `.txt` file.
4. The program calculates:
   - Word count
   - Character count
   - Line count
   - Sentence count (using regex for `.`, `!`, `?`)
5. Results are displayed in a formatted output.

## 💻 Example Output

```text
🟪 WORD COUNTER 🟪
1. Enter text manually
2. Read from a text file
Enter your choice (1/2): 1
Enter your text below (type 'END' on a new line to finish):
Hello world!
This is a test.
END

🟩 RESULTS 🟩
Words: 5
Characters: 28
Lines: 2
Sentences: 2
```

*Counts vary depending on the input text.*

## 🧠 What I Learned

- Splitting text into words and lines
- Using regex to detect sentences
- Handling file input and errors
- Writing modular functions
- Building a practical text analysis tool

## ▶️ How to Run

```bash
python main.py
```

Make sure the text file is in the same directory if using file input.

## 📁 Project Structure

```text
DayX_WordCounter/
│
├── main.py
└── README.md
```
#🚀 50 Days 50 Python Mini Projects
## 👨‍💻 Author

**Omm Prakash Pradhan**
B.Tech AI & ML Student

**Day 24/50** — Learn • Build • Improve

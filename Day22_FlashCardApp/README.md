# 🧠 Day 22 - Flashcard App

A Python program that allows users to create, view, and test flashcards for effective learning and revision.

## 🎯 Objective

To create a Flashcard App that helps users study and memorize information interactively using question‑answer flashcards.

## 🛠️ Concepts Used

- Lists
- Dictionaries
- Loops
- Conditional Statements
- File Handling (JSON)
- Functions
- User Input

## 📚 Required Libraries

This project uses Python’s built‑in libraries:

- `json`
- `os`

No external libraries are required.

## ⚙️ How It Works

1. The program loads existing flashcards from a JSON file.
2. Users can add new flashcards by entering questions and answers.
3. Flashcards are saved automatically to the JSON file.
4. Users can view all stored flashcards.
5. The “Test Yourself” mode displays questions and reveals answers interactively.
6. The program calculates the user’s score based on known answers.
7. The menu runs in a loop until the user chooses to exit.

## 💻 Example Output

```text
===== FLASHCARD App =====
1. Add Flashcard
2. View Flashcards
3. Test Yourself
4. Exit
Enter choice (1-4): 1
Enter question: What is the capital of France?
Enter answer: Paris

Flashcard added successfully!

===== FLASHCARD App =====
1. Add Flashcard
2. View Flashcards
3. Test Yourself
4. Exit
Enter choice (1-4): 3

FLASHCARD TEST
Q1: What is the capital of France? (Press Enter to reveal answer)
Answer: Paris
Did you know this? (y/n): y

Your Score: 1 out of 1
```

*Flashcards are saved in `flashcards.json` and persist between runs.*

## 🧠 What I Learned

- Using JSON for data storage
- Reading and writing files in Python
- Creating menu‑driven programs
- Handling user input and validation
- Building interactive learning tools
- Applying loops and functions effectively

## ▶️ How to Run

```bash
python main.py
```

Make sure the program has permission to read/write files in the working directory.

## 📁 Project Structure

```text
DayX_FlashcardApp/
│
├── main.py
├── flashcards.json
└── README.md
```
#🚀 50 Days 50 Python Mini Projects
## 👨‍💻 Author

**Omm Prakash Pradhan**
B.Tech AI & ML Student

**Day 22/50** — Learn • Build • Improve


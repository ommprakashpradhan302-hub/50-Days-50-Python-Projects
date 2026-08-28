# 📋 Day 19 - Attendance System

A Python program that manages student attendance by marking presence, viewing records, and calculating attendance percentages.

## 🎯 Objective

To create an Attendance System that allows users to record attendance, view attendance logs, and calculate attendance percentages in a simple and efficient way.

## 🛠️ Concepts Used

- Dictionaries
- Loops
- Conditional Statements
- File Handling (JSON)
- User Input
- Functions
- Error Handling

## 📚 Required Libraries

This project uses Python’s built-in libraries:

- `json`
- `os`

No external libraries are required.

## ⚙️ How It Works

1. The program loads existing attendance data from a JSON file.
2. Users can mark attendance by entering a student’s name.
3. Attendance records are saved and updated in the JSON file.
4. Users can view attendance records for all students.
5. Users can calculate attendance percentages based on total working days.
6. Invalid inputs are handled with error messages.
7. The program runs in a menu-driven loop until the user chooses to exit.

## 💻 Example Output

```text
===== ATTENDANCE SYSTEM MENU =====
1. Mark Attendance
2. View Attendance
3. Calculate Percentage
4. Exit
Enter your choice (1-4): 1
Enter student name: Alice
Attendance marked for Alice!

===== ATTENDANCE SYSTEM MENU =====
1. Mark Attendance
2. View Attendance
3. Calculate Percentage
4. Exit
Enter your choice (1-4): 2

--- ATTENDANCE RECORDS ---
Alice: 1 day(s) present
```

*Attendance records are saved in `attendance.json` and persist between runs.*

## 🧠 What I Learned

- Using JSON for persistent data storage
- Reading and writing files in Python
- Creating menu-driven programs
- Handling user input and errors
- Performing calculations with dictionaries
- Building a practical utility for classroom management

## ▶️ How to Run

```bash
python main.py
```

Make sure the program has permission to read/write files in the working directory.

## 📁 Project Structure

```text
DayX_AttendanceSystem/
│
├── main.py
├── attendance.json
└── README.md
```
#🚀 50 Days 50 Python Mini Projects
## 👨‍💻 Author

**Omm Prakash Pradhan**
B.Tech AI & ML Student

**Day 19/50** — Learn • Build • Improve


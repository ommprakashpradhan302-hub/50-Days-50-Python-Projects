# 🔐 Day 25 - Password Strength Checker

A Python program that evaluates the strength of a password based on multiple criteria and provides feedback to the user.

## 🎯 Objective

To create a Password Strength Checker that helps users build secure passwords by analyzing length, character variety, and complexity.

## 🛠️ Concepts Used

- String Methods
- Loops
- Conditional Statements
- Functions
- User Input
- Output Formatting

## 📚 Required Libraries

This project uses Python’s built‑in features.  
No external libraries are required.

## ⚙️ How It Works

1. The user enters a password.
2. The program checks the password against five criteria:
   - Minimum length (≥ 8 characters)
   - Contains lowercase letters
   - Contains uppercase letters
   - Contains digits
   - Contains special symbols
3. A score is calculated out of 5.
4. Based on the score, the program assigns a strength level:
   - Weak
   - Medium
   - Strong
   - Very Strong
5. Feedback is displayed to help the user improve their password.

## 💻 Example Output

```text
Enter your password: abc
========== PASSWORD STRENGTH REPORT ==========
Strength : Weak
Score : 1/5
Feedback : Use at least 8 characters with mix of letters, numbers and symbols.
==============================================

Enter your password: MyPass123!
========== PASSWORD STRENGTH REPORT ==========
Strength : Very Strong
Score : 5/5
Feedback : Excellent! Your password is very strong.
==============================================
```

*Strength levels vary depending on the entered password.*

## 🧠 What I Learned

- Using string methods like `.islower()`, `.isupper()`, `.isdigit()`
- Checking for special characters in strings
- Writing reusable functions
- Applying conditional logic for scoring
- Formatting output for clarity
- Building a practical security utility

## ▶️ How to Run

```bash
python main.py
```

No internet connection is required since checks are performed locally.

## 📁 Project Structure

```text
DayX_PasswordStrengthChecker/
│
├── main.py
└── README.md
```
#🚀 50 Days 50 Python Mini Projects
## 👨‍💻 Author

**Omm Prakash Pradhan**
B.Tech AI & ML Student

**Day 25/50** — Learn • Build • Improve

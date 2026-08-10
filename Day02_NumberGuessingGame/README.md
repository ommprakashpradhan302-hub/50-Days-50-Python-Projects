# 🎯 Number Guessing Game

A simple Python game where the computer randomly selects a number between 1 and 100, and the user tries to guess it.

This project is **Day 2** of my **50 Days 50 Python Mini Projects** challenge.

## 🚀 Features

- 🎲 Generates a random number between 1 and 100
- ⌨️ Takes guesses from the user
- 💡 Gives hints if the guess is too high or too low
- 🔢 Counts the number of attempts
- 🎉 Displays a congratulation message when the correct number is guessed

## 🛠️ Technologies Used

- **Python 3**
- `random` module
- `while` loop
- `if / elif / else`
- User input and output

## 📚 Concepts Learned

- Generating random numbers
- Using the `random` module
- Using loops
- Using conditional statements
- Taking user input
- Building basic game logic
- Counting attempts

## 📂 Project Structure

```text
Day-02-Number-Guessing-Game/
│
├── number_guessing_game.py
└── README.md
```

## ▶️ How to Run

Make sure Python 3 is installed on your computer.

Open the terminal inside the project folder and run:

```bash
python number_guessing_game.py
```

## 💻 Example Code

```python
import random

print("🎯 Welcome to the Number Guessing Game! 🎯")
print("I have selected a number between 1 and 100.")

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")

    elif guess > number:
        print("Too high! Try again.")

    else:
        print(f"🎉 Congratulations! You guessed the number {number}.")
        print(f"You took {attempts} attempts.")
        break
```

## 🖥️ Example Output

```text
🎯 Welcome to the Number Guessing Game! 🎯
I have selected a number between 1 and 100.

Enter your guess: 50
Too low! Try again.

Enter your guess: 75
Too high! Try again.

Enter your guess: 68
🎉 Congratulations! You guessed the number 68.
You took 3 attempts.
```

> **Note:** The number is randomly generated, so the output will be different each time you run the program.

## 🎯 What I Learned

This project helped me understand random number generation, loops, conditional statements, user input, and basic interactive game logic in Python.

## 📅 50 Days 50 Python Mini Projects

| Day | Project | Status |
|---|---|---|
| 01 | Simple Calculator | ✅ Completed |
| 02 | Number Guessing Game | ✅ Completed |
| 03 | Coming Soon | ⏳ |
| ... | ... | ... |
| 50 | Coming Soon | ⏳ |

## 👨‍💻 Author

**Omm Prakash Pradhan**

B.Tech AI & ML Student

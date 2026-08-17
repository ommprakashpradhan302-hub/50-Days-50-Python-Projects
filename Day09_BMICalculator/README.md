# 🧮 BMI Calculator

A simple Python BMI Calculator that takes weight and height as input, calculates Body Mass Index (BMI), and displays the result with a category.

This project is **Day 9** of my **50 Days 50 Python Mini Projects** challenge.

## 🚀 Features

- ⚖️ Takes weight in kilograms
- 📏 Takes height in meters
- 🧮 Calculates BMI using a mathematical formula
- 📊 Displays BMI rounded to two decimal places
- 📝 Displays a BMI category
- ⚠️ Validates positive input values
- 🛡️ Handles invalid numeric input using exception handling

## 🛠️ Technologies Used

- **Python 3**
- No external libraries required

## 📚 Concepts Learned

- Taking multiple user inputs
- Converting input to `float`
- Performing mathematical calculations
- Using the BMI formula
- Using `if-elif-else` statements
- Formatting numerical output
- Handling `ValueError` with `try-except`
- Validating user input

## 📂 Project Structure

```text
Day-09-BMI-Calculator/
│
├── main.py
└── README.md
```

## ▶️ How to Run

Make sure Python 3 is installed on your computer.

Open the terminal inside the project folder and run:

```bash
python main.py
```

Enter your weight in kilograms and height in meters when prompted.

## 🧮 Formula

```text
BMI = weight (kg) / height (m)²
```

## 🖥️ Example Output

```text
💪 Welcome to BMI Calculator 💪
Enter your weight in kilograms (kg): 70
Enter your height in meters (m): 1.75

Your BMI is: 22.86
Category: Normal weight
```

### Invalid Input Example

```text
Enter your weight in kilograms (kg): -50
Enter your height in meters (m): 1.70

Weight and height must be greater than zero.
```

> **Note:** BMI is a general screening measure and is not a complete measure of health.

## 🎯 What I Learned

This project helped me understand how to take multiple inputs, perform calculations using a formula, validate input, use conditional statements, format numerical results, and handle errors in Python.

## 👨‍💻 Author

**Omm Prakash Pradhan**

B.Tech AI & ML Student

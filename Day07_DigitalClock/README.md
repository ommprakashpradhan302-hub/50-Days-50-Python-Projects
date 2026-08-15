# 🕐 Digital Clock

A digital clock that displays the current time in `HH:MM:SS` format and updates every second.

This project is **Day 7** of my **50 Days 50 Python Mini Projects** challenge.

## 🚀 Features

- 🕒 Displays the current time in `HH:MM:SS` format
- 🔄 Updates the time every second
- ♾️ Runs continuously using an infinite loop
- 🖨️ Prints the time on the same line for a live clock effect
- ⌨️ Handles keyboard interrupt (`Ctrl+C`) gracefully
- 🛑 Displays a message when the clock is stopped

## 🛠️ Technologies Used

- **Python 3**
- `time` module

The `time` module is built into Python, so no external installation is required.

## 📚 Concepts Learned

- Importing and using the `time` module
- Getting the current time with `time.strftime()`
- Using an infinite `while` loop
- String formatting with f-strings
- Using `time.sleep()`
- Handling `KeyboardInterrupt` exceptions
- Formatting output on a single line

## 📂 Project Structure

```text
Day-07-Digital-Clock/
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

## 🖥️ Example Output

```text
Digital Clock Started. Press Ctrl+C to stop.
Current Time: 14:25:30
Current Time: 14:25:31
Current Time: 14:25:32
Current Time: 14:25:33
Current Time: 14:25:34
Current Time: 14:25:35
...
(Press Ctrl+C to stop)
```

> **Note:** The clock keeps updating every second until it is manually stopped with `Ctrl+C`.

## 🎯 What I Learned

This project helped me understand how to work with the `time` module, format and display time, use infinite loops, and handle keyboard interrupts in Python.

## 👨‍💻 Author

**Omm Prakash Pradhan**

B.Tech AI & ML Student

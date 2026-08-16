# ⏰ Alarm Clock

A simple Python alarm clock that takes an alarm time from the user and continuously checks the current time until it matches the set alarm time.

This project is **Day 8** of my **50 Days 50 Python Mini Projects** challenge.

## 🚀 Features

- ⏰ Allows the user to set an alarm time
- 🕐 Uses 24-hour time format (`HH:MM:SS`)
- 🔄 Continuously checks the current time
- ⚡ Triggers an alarm message when the times match
- 🛑 Stops automatically after the alarm is triggered

## 🛠️ Technologies Used

- **Python 3**
- `datetime` module
- `time` module

Both modules are built into Python, so no external installation is required.

## 📚 Concepts Learned

- Working with the `datetime` module
- Working with the `time` module
- Taking user input
- Getting and formatting the current time
- Using `while` loops
- Comparing time values
- Using `time.sleep()`
- Triggering an alert when a condition is met
- Using `break` to stop a loop

## 📂 Project Structure

```text
Day-08-Alarm-Clock/
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

When prompted, enter the alarm time in **24-hour format**:

```text
HH:MM:SS
```

For example:

```text
07:30:00
```

## 🖥️ Example Output

```text
⏰ Welcome to Alarm Clock ⏰
Enter alarm time (HH:MM:SS in 24-hour format): 07:30:00
Alarm set for 07:30:00

Current Time: 07:29:57
Current Time: 07:29:58
Current Time: 07:29:59
Current Time: 07:30:00

⏰ Time to Wake Up! ⏰
Alarm! Alarm! Alarm!
Alarm Stopped. Have a Great Day! 😊
```

> **Note:** The current time and alarm time will depend on when you run the program.

## 🎯 What I Learned

This project helped me understand how to work with `datetime` and `time`, take user input, continuously check conditions using loops, compare time values, and trigger an alert when the specified time is reached.

## 👨‍💻 Author

**Omm Prakash Pradhan**

B.Tech AI & ML Student

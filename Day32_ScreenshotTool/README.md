# 📸 Day 32 - Screenshot Tool

A Python program that captures a screenshot of the entire screen and saves it as an image file.

## 🎯 Objective

To create a Screenshot Tool that allows users to capture their screen and save it automatically with a timestamped filename.

## 🛠️ Concepts Used

- Screen Capture  
- File Handling  
- OS Module  
- Date & Time  
- Exception Handling  
- User Input  
- pyautogui Library

## 📚 Required Libraries

This project uses the third‑party `pyautogui` library.  

Install it using:

```bash
pip install pyautogui
```

## ⚙️ How It Works

1. The program captures a screenshot of the entire screen using `pyautogui.screenshot()`.  
2. If no output folder is provided, a default folder named **screenshots** is created.  
3. A unique filename is generated using the current date and time.  
4. The screenshot is saved as a `.png` file in the output folder.  
5. The program displays the file location after saving.  
6. Errors are handled gracefully with exception messages.

## 💻 Example Output

```text
✅ Screenshot saved successfully!
📁 File location: C:\Users\OMM\screenshots\screenshot_2026-09-10_22-32-00.png
```

*Each screenshot is saved with a unique timestamp to avoid overwriting.*

## 🧠 What I Learned

- Capturing screenshots with `pyautogui`  
- Creating folders dynamically with `os.makedirs`  
- Generating unique filenames using `datetime`  
- Handling exceptions for robust code  
- Building a practical utility for productivity

## ▶️ How to Run

```bash
python main.py
```

Make sure `pyautogui` is installed and the program has permission to save files in the chosen directory.

## 📁 Project Structure

```text
Day32_ScreenshotTool/
│
├── main.py
└── README.md
```
#🚀 50 Days 50 Python Mini Projects
## 👨‍💻 Author

**Omm Prakash Pradhan**
B.Tech AI & ML Student

**Day 32/50** — Learn • Build • Improve


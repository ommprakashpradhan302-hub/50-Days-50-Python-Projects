# 🎥 Day 33 - Screen Recorder

A Python program that records the screen for a specified duration and saves it as an MP4 video file.

## 🎯 Objective

To create a Screen Recorder that captures the entire screen and saves it as a video file for tutorials, demos, or personal use.

## 🛠️ Concepts Used

- Screen Capture  
- File Handling  
- Loops  
- Conditional Statements  
- Exception Handling  
- OpenCV (`cv2`)  
- NumPy  
- Date & Time  
- User Input

## 📚 Required Libraries

This project uses the following libraries:

- `opencv-python`  
- `numpy`  

Install them using:

```bash
pip install opencv-python numpy
```

*(Note: `ImageGrab` from `PIL` or `pyautogui` may also be required depending on your environment.)*

## ⚙️ How It Works

1. The user specifies the recording duration in seconds.  
2. The program captures the screen frame by frame using `ImageGrab`.  
3. Frames are converted to BGR format for OpenCV.  
4. A `VideoWriter` object saves frames into an MP4 file.  
5. The recording stops after the specified duration.  
6. The video file is saved with a timestamped filename.  
7. Errors are handled gracefully with exception messages.

## 💻 Example Output

```text
Enter recording duration in seconds: 5
🔴 Recording started for 5 seconds...
🟢 Recording stopped and saved successfully!
📁 Video saved as: screen_recording_2026-09-11_21-19-00.mp4
```

*The screen is recorded for the given duration and saved as an MP4 file.*

## 🧠 What I Learned

- Capturing screen frames with `ImageGrab`  
- Writing video files with OpenCV’s `VideoWriter`  
- Using NumPy arrays for image processing  
- Handling exceptions for robust code  
- Automating screen recording tasks

## ▶️ How to Run

```bash
python main.py
```

Make sure required libraries are installed and the program has permission to capture the screen.

## 📁 Project Structure

```text
Day33_ScreenRecorder/
│
├── main.py
└── README.md
```
#🚀 50 Days 50 Python Mini Projects
## 👨‍💻 Author

**Omm Prakash Pradhan**
B.Tech AI & ML Student

**Day 33/50** — Learn • Build • Improve

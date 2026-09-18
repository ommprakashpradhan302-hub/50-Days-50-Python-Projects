# 👤 Day 39 - Face Detection

A Python program that detects human faces in an image or live webcam video using OpenCV.

## 🎯 Objective

To create a Face Detection tool that identifies and highlights human faces in real time using computer vision techniques.

## 🛠️ Concepts Used

- Computer Vision  
- Haar Cascade Classifier  
- Webcam Input  
- Image Processing  
- Exception Handling  
- OpenCV Library  

## 📚 Required Libraries

This project uses the third‑party `opencv-python` library.  

Install it using:

```bash
pip install opencv-python
```

## ⚙️ How It Works

1. Load the pre‑trained Haar Cascade classifier for face detection.  
2. Capture frames from the webcam (or load an image).  
3. Convert frames to grayscale for better accuracy.  
4. Detect faces using `detectMultiScale()`.  
5. Draw rectangles around detected faces.  
6. Display the output in a window.  
7. Press **q** to quit the program.  

## 💻 Example Output

```text
🟢 Press 'q' to quit
✅ Detected faces highlighted with rectangles
```

*Faces in the webcam feed or image are marked with green rectangles.*

## 🧠 What I Learned

- Using Haar Cascade classifiers for face detection  
- Capturing video frames with OpenCV  
- Converting images to grayscale for processing  
- Drawing shapes on images with OpenCV  
- Building a real‑world computer vision application  

## ▶️ How to Run

```bash
python main.py
```

Make sure your webcam is connected and `opencv-python` is installed.

## 📁 Project Structure

```text
Day39_FaceDetection/
│
├── main.py
└── README.md
```

## 🚀 50 Days 50 Python Mini Projects

👨‍💻 Author: **Omm Prakash Pradhan**  
B.Tech AI & ML Student

**Day 39/50** — Learn • Build • Detect

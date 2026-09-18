# 🗣️ Day 38 - Speech-to-Text Converter

A Python program that converts spoken voice input into text using the microphone and Google Speech Recognition.

## 🎯 Objective

To create a Speech-to-Text Converter that allows users to speak through a microphone and automatically convert their speech into written text.

## 🛠️ Concepts Used

- Functions  
- Exception Handling  
- User Input  
- Microphone Input  
- Speech Recognition  
- `SpeechRecognition` Library  
- `PyAudio` Library  
- Google Speech Recognition API  

## 📚 Required Libraries

This project uses the third‑party `SpeechRecognition` and `PyAudio` libraries.  

Install them using:

```bash
pip install SpeechRecognition
pip install PyAudio
```

Or install both together:

```bash
pip install SpeechRecognition PyAudio
```

## ⚙️ How It Works

1. The program initializes the `SpeechRecognition` recognizer.  
2. The microphone is used as the audio input source.  
3. The program adjusts itself according to the surrounding background noise.  
4. The user speaks into the microphone.  
5. The recorded audio is sent to Google’s Speech Recognition service.  
6. The recognized speech is converted into text.  
7. The converted text is displayed on the screen.  
8. Errors are handled gracefully if the speech cannot be understood or the recognition service cannot be reached.  

## 💻 Example Output

```text
=== SPEECH-TO-TEXT CONVERTER ===

🎤 Listening... Speak something!
🔄 Recognizing...
✅ You said: Hello, this is my speech to text converter.
```

*An active microphone and internet connection are required for speech recognition.*

## 🧠 What I Learned

- Using `SpeechRecognition` for converting speech into text  
- Capturing audio through a microphone  
- Using `PyAudio` for microphone input  
- Handling background noise for better accuracy  
- Using Google’s Speech Recognition service  
- Handling `UnknownValueError` and `RequestError`  
- Building a practical voice‑based Python application  

## ▶️ How to Run

First, install the required libraries:

```bash
pip install SpeechRecognition PyAudio
```

Then run the program:

```bash
python main.py
```

Make sure your microphone is connected and working properly.  
An active internet connection is also required because the program uses Google’s Speech Recognition service.

## 📁 Project Structure

```text
Day38_SpeechToTextConverter/
│
├── main.py
└── README.md
```

## 🚀 50 Days 50 Python Mini Projects


👨‍💻 Author: **Omm Prakash Pradhan**  
B.Tech AI & ML Student

**Day 38/50** — Learn • Build • Improve

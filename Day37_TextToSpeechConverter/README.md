# 🗣️ Day 37 - Text-to-Speech Converter

A Python program that converts text input into natural speech and saves it as an audio file.

## 🎯 Objective

To create a Text-to-Speech Converter that allows users to transform written text into spoken audio.

## 🛠️ Concepts Used

- Functions  
- Exception Handling  
- User Input  
- File Handling  
- pyttsx3 Library  

## 📚 Required Libraries

This project uses the third‑party `pyttsx3` library.  

Install it using:

```bash
pip install pyttsx3
```

## ⚙️ How It Works

1. The user enters text to be converted into speech.  
2. The program initializes the `pyttsx3` engine.  
3. Voice properties (rate, voice ID) can be customized.  
4. The text is spoken aloud and saved as an audio file (`output.mp3`).  
5. The audio file can be played in any media player.  
6. Errors are handled gracefully with exception messages.

## 💻 Example Output

```text
=== TEXT-TO-SPEECH CONVERTER ===
Enter the text you want to convert to speech:
> Hello! This is a text-to-speech converter created using Python.
✅ Speech saved successfully as 'output.mp3'
```

*The generated audio file can be played in any standard media player.*

## 🧠 What I Learned

- Using `pyttsx3` for speech synthesis  
- Customizing voice properties (rate, voice ID)  
- Saving spoken text as an audio file  
- Handling exceptions for robust code  
- Building a practical accessibility tool  

## ▶️ How to Run

```bash
python main.py
```

Make sure `pyttsx3` is installed and your system supports audio playback.

## 📁 Project Structure

```text
Day37_TextToSpeechConverter/
│
├── main.py
└── README.md
```
#🚀 50 Days 50 Python Mini Projects
## 👨‍💻 Author

**Omm Prakash Pradhan**
B.Tech AI & ML Student

**Day 37/50** — Learn • Build • Improve


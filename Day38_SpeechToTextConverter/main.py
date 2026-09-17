import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\n🎤 Listening... Speak something!")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("🔄 Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"✅ You said: {text}")

    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")

    except sr.RequestError as e:
        print(f"❌ Could not request results; {e}")


if __name__ == "__main__":
    print("=== SPEECH-TO-TEXT CONVERTER ===")
    speech_to_text()
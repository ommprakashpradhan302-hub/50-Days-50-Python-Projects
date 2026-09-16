import pyttsx3

def speak_text(text, filename="output.mp3", rate=150, voice_id=None):
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')

        if voice_id is not None and 0 <= voice_id < len(voices):
            engine.setProperty('voice', voices[voice_id].id)

        engine.setProperty('rate', rate)      # Speed of speech
        engine.say(text)                      # Convert text to speech
        engine.save_to_file(text, filename)   # Save to audio file
        engine.runAndWait()                   # Process and save

        print(f"\n✅ Speech saved successfully as '{filename}'")
    except Exception as e:
        print(f"\n❌ Error: {e}")

def main():
    print("=== TEXT-TO-SPEECH CONVERTER ===")
    text = input("Enter the text you want to convert to speech:\n ")
    speak_text(text)

if __name__ == "__main__":
    main()

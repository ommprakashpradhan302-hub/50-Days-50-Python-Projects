import cv2
import numpy as np
import datetime
import time
from PIL import ImageGrab  # Needed for screen capture

def record_screen(duration, output_file):
    # Get screen size (adjust if your screen resolution is different)
    screen_width = 1920
    screen_height = 1080

    # Define codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (screen_width, screen_height))

    print(f"🔴 Recording started for {duration} seconds...")
    start_time = time.time()
    try:
        while int(time.time() - start_time) < duration:
            # Capture the screen
            screenshot = np.array(ImageGrab.grab(bbox=(0, 0, screen_width, screen_height)))
            screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

            # Write frame to video file
            out.write(screenshot)
    except Exception as e:
        print(f"⚠️ Error: {e}")
    finally:
        out.release()
        print("🟢 Recording stopped and saved successfully!")
        print(f"🎥 Video saved as: {output_file}")

if __name__ == "__main__":
    duration = int(input("Enter recording duration in seconds: "))
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"screen_recording_{timestamp}.mp4"
    record_screen(duration, output_file)

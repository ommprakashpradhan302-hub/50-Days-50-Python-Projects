import pyautogui
import datetime
import os

def take_screenshot(output_folder=None):
    try:
        # Take screenshot of the entire screen
        screenshot = pyautogui.screenshot()

        # Create output folder if not provided
        if output_folder is None:
            output_folder = "screenshots"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Create filename with current date and time
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_path = os.path.join(output_folder, f"screenshot_{timestamp}.png")

        # Save the screenshot
        screenshot.save(file_path)
        print("✅ Screenshot saved successfully!")
        print(f"📁 File location: {os.path.abspath(file_path)}")
        return file_path

    except Exception as e:
        print(f"❌ Error: {e}")
        return None

if __name__ == "__main__":
    take_screenshot()

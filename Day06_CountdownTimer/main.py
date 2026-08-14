import time

print("⏳ Welcome to Countdown Timer! ⏳")

try:
    seconds = int(input("👉 Enter time in seconds: "))
    
    if seconds < 0:
        print("⚠️ Please enter a positive number.")
    else:
        print("🚀 Countdown Started...\n")
        while seconds >= 0:
            mins, secs = divmod(seconds, 60)
            timer = f"{mins:02d}:{secs:02d}"
            print(timer, end="\r")  # overwrite the same line
            time.sleep(1)
            seconds -= 1
        
        print("00:00")
        print("🎉 Time's up! 🎉")
except ValueError:
    print("⚠️ Please enter a valid number.")

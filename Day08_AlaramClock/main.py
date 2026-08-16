from datetime import datetime
import time

print("⏰ Welcome to Alarm Clock! ⏰")

# Ask user for alarm time
alarm_time = input("👉 Enter alarm time (HH:MM:SS in 24-hour format): ")
print(f"🕒 Alarm set for {alarm_time}")

while True:
    now = datetime.now().strftime("%H:%M:%S")
    print(f"\r⌛ Current Time: {now}", end="")

    if now == alarm_time:
        print("\n🔔 Time to Wake Up! 🔔")
        print("🎉 Alarm! Alarm! 🎉")
        break

    time.sleep(1)

print("👋 Alarm Stopped. Have a Great Day! 🌞")

import time

def digital_clock(format_12=False):
    """Displays the current time in HH:MM:SS format (24h or 12h)."""
    try:
        while True:
            if format_12:
                current_time = time.strftime("%I:%M:%S %p")  # 12-hour format with AM/PM
            else:
                current_time = time.strftime("%H:%M:%S")      # 24-hour format
            
            print(f"\r⏰ Current Time: {current_time}", end="")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Clock stopped.")

# Run the clock
print("🕒 Digital Clock Started.")
choice = input("👉 Do you want 12-hour format? (y/n): ").lower()

if choice == "y":
    digital_clock(format_12=True)
else:
    digital_clock(format_12=False)

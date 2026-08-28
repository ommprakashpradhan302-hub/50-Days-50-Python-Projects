# Attendance System
import json, os
FILE = "attendance.json"

def load_data():
    if os.path.exists(FILE):
        with open(FILE, 'r') as f:
            return json.load(f)
    else:
        return {}

def save_data(data):
    with open(FILE, 'w') as f:
        json.dump(data, f, indent=4)

def mark_attendance(data):
    name = input("Enter student name: ").strip()
    if name in data:
        data[name] += 1
        print(f"Attendance marked for {name}!")
    else:
        data[name] = 1
        print(f"{name} added and attendance marked!")

def view_attendance(data):
    if not data:
        print("No attendance records found.")
    else:
        print("\n--- ATTENDANCE RECORDS ---")
        for name, count in data.items():
            print(f"{name}: {count} day(s) present")

def calculate_percentage(data, total_days):
    if not data or total_days == 0:
        print("No records found or total days is zero.")
        return
    print("\n--- ATTENDANCE PERCENTAGE ---")
    for name, count in data.items():
        percentage = (count / total_days) * 100
        print(f"{name}: {percentage:.2f}%")

def main():
    data = load_data()
    while True:
        print("\n===== ATTENDANCE SYSTEM MENU =====")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Calculate Percentage")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            mark_attendance(data)
            save_data(data)
        elif choice == '2':
            view_attendance(data)
        elif choice == '3':
            total_days = int(input("Enter total number of working days: "))
            calculate_percentage(data, total_days)
        elif choice == '4':
            print("Thank you! Exiting...")
            break
        else:
            print("Invalid choice! Please select between 1 and 4.")

if __name__ == "__main__":
    main()

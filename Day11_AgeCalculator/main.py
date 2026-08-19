from datetime import date, timedelta

print("🎂 Welcome to Age Calculator 📅")

day = int(input("👉 Enter your birth day (DD): "))
month = int(input("👉 Enter your birth month (MM): "))
year = int(input("👉 Enter your birth year (YYYY): "))

today = date.today()
birth_date = date(year, month, day)

years = today.year - birth_date.year
months = today.month - birth_date.month
days = today.day - birth_date.day

if days < 0:
    months -= 1
    prev_month = date(today.year, today.month, 1) - timedelta(days=1)
    days += prev_month.day

if months < 0:
    years -= 1
    months += 12

print(f"🎉 Your Age is: {years} years, {months} months, {days} days.")

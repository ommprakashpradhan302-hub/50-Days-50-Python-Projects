# BMI Calculator
print("💪 Welcome to BMI Calculator 🧮")

try:
    weight = float(input("⚖️ Enter your weight in kilograms (kg): "))
    height = float(input("📏 Enter your height in meters (m): "))

    if weight <= 0 or height <= 0:
        print("⚠️ Weight and height must be greater than zero.")
    else:
        bmi = weight / (height ** 2)
        print(f"📊 Your BMI is: {bmi:.2f}")

        print("📌 Category:", end=" ")

        if bmi < 18.5:
            print("🍃 Underweight")
        elif 18.5 <= bmi < 24.9:
            print("✅ Normal weight")
        elif 25 <= bmi < 29.9:
            print("⚠️ Overweight")
        else:
            print("🔥 Obese")

except ValueError:
    print("⚠️ Please enter valid numbers.")

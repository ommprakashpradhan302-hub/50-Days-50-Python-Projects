# Temperature Converter
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

print("🌡️ TEMPERATURE CONVERTER 🌡️")
print("1. Celsius ➡️ Fahrenheit")
print("2. Celsius ➡️ Kelvin")
print("3. Fahrenheit ➡️ Celsius")
print("4. Fahrenheit ➡️ Kelvin")
print("5. Kelvin ➡️ Celsius")
print("6. Kelvin ➡️ Fahrenheit")
print("7. Exit")

while True:
    choice = input("👉 Choose an option (1-7): ")

    if choice in ['1','2','3','4','5','6']:
        value = float(input("Enter temperature value: "))

        if choice == '1':
            result = celsius_to_fahrenheit(value)
            unit = "°F"
        elif choice == '2':
            result = celsius_to_kelvin(value)
            unit = "K"
        elif choice == '3':
            result = fahrenheit_to_celsius(value)
            unit = "°C"
        elif choice == '4':
            result = fahrenheit_to_kelvin(value)
            unit = "K"
        elif choice == '5':
            result = kelvin_to_celsius(value)
            unit = "°C"
        elif choice == '6':
            result = kelvin_to_fahrenheit(value)
            unit = "°F"

        print(f"✅ Converted Value: {result:.2f} {unit}\n")

    elif choice == '7':
        print("👋 Goodbye! Stay cool ❄️ or warm 🔥!")
        break
    else:
        print("⚠️ Invalid choice! Please try again.\n")

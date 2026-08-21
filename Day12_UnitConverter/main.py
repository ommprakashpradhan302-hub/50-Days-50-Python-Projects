# Unit Converter Program

def length_converter():
    print("\n=== Length Converter ===")
    print("1. Kilometers to Meters")
    print("2. Meters to Kilometers")
    choice = input("Choose an option (1/2): ")
    value = float(input("Enter value: "))

    if choice == '1':
        result = value * 1000
        print(f"{value} km = {result} meters")
    elif choice == '2':
        result = value / 1000
        print(f"{value} meters = {result} km")
    else:
        print("Invalid choice!")

def weight_converter():
    print("\n=== Weight Converter ===")
    print("1. Kilograms to Grams")
    print("2. Grams to Kilograms")
    choice = input("Choose an option (1/2): ")
    value = float(input("Enter value: "))

    if choice == '1':
        result = value * 1000
        print(f"{value} kg = {result} grams")
    elif choice == '2':
        result = value / 1000
        print(f"{value} grams = {result} kg")
    else:
        print("Invalid choice!")

def temp_converter():
    print("\n=== Temperature Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose an option (1/2): ")
    value = float(input("Enter value: "))

    if choice == '1':
        result = (value * 9/5) + 32
        print(f"{value}°C = {result:.2f}°F")
    elif choice == '2':
        result = (value - 32) * 5/9
        print(f"{value}°F = {result:.2f}°C")
    else:
        print("Invalid choice!")

# Main Menu
while True:
    print("\n=== UNIT CONVERTER ===")
    print("1. Length Converter")
    print("2. Weight Converter")
    print("3. Temperature Converter")
    print("4. Exit")

    option = input("Choose an option (1-4): ")

    if option == '1':
        length_converter()
    elif option == '2':
        weight_converter()
    elif option == '3':
        temp_converter()
    elif option == '4':
        print("Thank you for using Unit Converter! 😊")
        break
    else:
        print("Invalid option! Please try again.")

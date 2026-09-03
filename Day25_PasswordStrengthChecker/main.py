def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for c in password):
        score += 1

    if score <= 2:
        strength = "Weak"
        feedback = "Use at least 8 characters with a mix of letters, numbers, and symbols."
    elif score == 3:
        strength = "Medium"
        feedback = "Good! Add more variety (uppercase, numbers, symbols)."
    elif score == 4:
        strength = "Strong"
        feedback = "Great! Your password is strong."
    else:
        strength = "Very Strong"
        feedback = "Excellent! Your password is very strong."

    return strength, feedback, score

def main():
    password = input("Enter your password: ")
    strength, feedback, score = check_password_strength(password)

    print("========== PASSWORD STRENGTH REPORT ==========")
    print(f"Strength : {strength}")
    print(f"Score    : {score}/5")
    print(f"Feedback : {feedback}")
    print("==============================================")

if __name__ == "__main__":
    main()

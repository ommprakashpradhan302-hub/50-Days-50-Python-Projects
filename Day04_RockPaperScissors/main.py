import random

choices = ["rock", "paper", "scissors"]
user = input("Enter your choice (rock 🪨 / paper 📄 / scissors ✂️): ").lower()
computer = random.choice(choices)

print(f"You chose: {user}")
print(f"Computer chose: {computer}")

if user == computer:
    print("🤝 It's a Tie!")
elif user == "rock":
    if computer == "scissors":
        print("🎉 Congratulations! You Win! 🏆")
    else:
        print("😢 You Lose!")
elif user == "paper":
    if computer == "rock":
        print("🎉 Congratulations! You Win! 🏆")
    else:
        print("😢 You Lose!")
elif user == "scissors":
    if computer == "paper":
        print("🎉 Congratulations! You Win! ✂️🏆")
    else:
        print("😢 You Lose!")
else:
    print("⚠️ Invalid choice! Please choose rock 🪨, paper 📄 or scissors ✂️.")

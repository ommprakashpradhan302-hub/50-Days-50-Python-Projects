# Quiz Game
def quiz_game():
    questions = [
        {"question": "Which planet is known as the Red Planet?",
         "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
         "answer": "B"},
        {"question": "What does CPU stand for?",
         "options": ["A. Central Processing Unit", "B. Computer Personal Unit", "C. Central Power Utility", "D. Control Processing Unit"],
         "answer": "A"},
        {"question": "Which data structure uses FIFO (First In First Out)?",
         "options": ["A. Stack", "B. Queue", "C. Array", "D. Linked List"],
         "answer": "B"},
        {"question": "Who is known as the father of electricity?",
         "options": ["A. Nikola Tesla", "B. Thomas Edison", "C. Benjamin Franklin", "D. Michael Faraday"],
         "answer": "D"},
        {"question": "Which keyword is used to create a loop in Python?",
         "options": ["A. loop", "B. repeat", "C. for", "D. iterate"],
         "answer": "C"}
    ]

    score = 0
    print("\n===== WELCOME TO THE QUIZ GAME! =====\n")

    for i, q in enumerate(questions, 1):
        print(f"{i}. {q['question']}")
        for option in q['options']:
            print(f"{option}")

        user_answer = input("Your answer (A/B/C/D): ").upper()
        if user_answer == q['answer']:
            print("✓ Correct!\n")
            score += 1
        else:
            print(f"✗ Wrong! Correct answer is {q['answer']}.\n")

    total = len(questions)
    print("===== QUIZ COMPLETED! =====")
    print(f"Your Score: {score} out of {total}")
    percentage = (score / total) * 100
    print(f"Percentage: {percentage:.2f}%")

    if percentage == 100:
        print("Excellent! Perfect Score! 🎉")
    elif percentage >= 60:
        print("Good job! Keep it up! 👍")
    else:
        print("Better luck next time! Try again. 😊")

if __name__ == "__main__":
    quiz_game()

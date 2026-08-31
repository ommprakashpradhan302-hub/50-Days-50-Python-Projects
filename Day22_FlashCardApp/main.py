import json, os
FILE = "flashcards.json"

def load_flashcards():
    if os.path.exists(FILE):
        with open(FILE, 'r') as f:
            return json.load(f)
    else:
        return []

def save_flashcards(cards):
    with open(FILE, 'w') as f:
        json.dump(cards, f, indent=4)

def add_flashcard(cards):
    question = input("Enter question: ").strip()
    answer = input("Enter answer: ").strip()
    cards.append({"question": question, "answer": answer})
    save_flashcards(cards)
    print("\n✅ Flashcard added successfully!\n")

def view_flashcards(cards):
    if not cards:
        print("\n⚠️ No flashcards available.\n")
        return
    print("\n📚 YOUR FLASHCARDS:\n")
    for i, card in enumerate(cards, 1):
        print(f"{i}. Q: {card['question']}")

def test_flashcards(cards):
    if not cards:
        print("\n⚠️ No flashcards to test.\n")
        return
    score = 0
    print("\n🧠 FLASHCARD TEST\n")
    for i, card in enumerate(cards, 1):
        input(f"Q{i}: {card['question']} (Press Enter to reveal answer)")
        print(f"Answer: {card['answer']}\n")
        know = input("Did you know this? (y/n): ").lower()
        if know == 'y':
            score += 1
    print(f"\nYour Score: {score} out of {len(cards)}\n")

def main():
    cards = load_flashcards()
    while True:
        print("\n===== FLASHCARD APP MENU =====")
        print("1. Add Flashcard")
        print("2. View Flashcards")
        print("3. Test Yourself")
        print("4. Exit")
        choice = input("Enter choice (1-4): ")

        if choice == '1':
            add_flashcard(cards)
        elif choice == '2':
            view_flashcards(cards)
        elif choice == '3':
            test_flashcards(cards)
        elif choice == '4':
            print("\n👋 Thank you for using Flashcard App. Goodbye!\n")
            break
        else:
            print("\n⚠️ Invalid choice! Please select between 1 and 4.\n")

if __name__ == "__main__":
    main()

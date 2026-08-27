# Random Joke Generator
import random

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "I told my computer I needed a break, and it said no problem—it would go to sleep.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "I would avoid the sushi if I was you. It's a little fishy.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I'm reading a book on anti-gravity. It's impossible to put down.",
    "Why don't programmers like nature? It has too many bugs.",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    "Why did the math book look sad? Because it had too many problems.",
    "Why do cows wear bells? Because their horns don’t work.",
    "Why did the computer go to the doctor? Because it caught a virus!",
    "Why did the bicycle fall over? Because it was two-tired.",
    "Why don’t eggs tell jokes? They’d crack each other up.",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
    "Why was the JavaScript developer sad? Because he didn’t know how to ‘null’ his feelings.",
    "Why did the programmer quit his job? Because he didn’t get arrays.",
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why did the student eat his homework? Because the teacher said it was a piece of cake."
]

def get_random_joke():
    return random.choice(jokes)

def main():
    print("😄 RANDOM JOKE GENERATOR 🤭")
    print("-" * 30)
    joke = get_random_joke()
    print(joke)
    print("-" * 30)
    again = input("\nWant another joke? (y/n): ").strip().lower()
    if again == 'y':
        main()
    else:
        print("Thanks for smiling! Have a great day! 😉")

if __name__ == "__main__":
    main()

# Random Quote Generator
import random

quotes = [
    "The only way to do great work is to love what you do.",
    "Believe you can and you're halfway there.",
    "The future depends on what you do today.",
    "Don't watch the clock; do what it does. Keep going.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "The best way to get started is to quit talking and begin doing.",
    "Dream it. Wish it. Do it.",
    "Little by little, one travels far.",
    "Stay positive, work hard, make it happen.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "Wake up with determination. Go to bed with satisfaction.",
    "Do something today that your future self will thank you for.",
    "It always seems impossible until it’s done.",
    "Hustle in silence and let your success make the noise.",
    "Doubt kills more dreams than failure ever will.",
    "Discipline is the bridge between goals and accomplishment."
]

def get_random_quote():
    return random.choice(quotes)

def main():
    print("\n" + "="*40)
    print(" RANDOM QUOTE GENERATOR ")
    print("="*40 + "\n")

    quote = get_random_quote()
    print("'" + quote + "'")
    print("\nKeep going and never give up! 💪")

if __name__ == "__main__":
    main()

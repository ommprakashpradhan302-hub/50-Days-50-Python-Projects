def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    return len(text)

def count_lines(text):
    lines = text.splitlines()
    return len(lines)

def count_sentences(text):
    import re
    # Count sentences by '.', '!' or '?'
    sentences = re.split(r'[.!?]+', text)
    # Filter out empty strings
    sentences = [s for s in sentences if s.strip()]
    return len(sentences)

def main():
    print("===== WORD COUNTER =====")
    print("1. Enter text manually")
    print("2. Read from a text file")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        print("Enter your text below (type 'END' on a new line to finish):")
        lines = []
        while True:
            line = input()
            if line.strip() == 'END':
                break
            lines.append(line)
        text = '\n'.join(lines)
    else:
        filename = input("Enter text file name (with .txt): ")
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                text = f.read()
        except FileNotFoundError:
            print("❌ Error: File not found!")
            return

    words = count_words(text)
    characters = count_characters(text)
    lines_count = count_lines(text)
    sentences = count_sentences(text)

    print("===== RESULTS =====")
    print(f"Words: {words}")
    print(f"Characters: {characters}")
    print(f"Lines: {lines_count}")
    print(f"Sentences: {sentences}")

if __name__ == "__main__":
    main()

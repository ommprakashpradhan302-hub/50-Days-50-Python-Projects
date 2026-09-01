def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "❌ Error: File not found!"
    except Exception as e:
        return f"❌ Error: {e}"

def main():
    print("📄 TEXT FILE READER 📄")
    print("=" * 30)
    filename = input("Enter the text file name (with .txt): ").strip()
    content = read_file(filename)

    print("\n" + "=" * 30)
    if content.startswith("❌ Error"):
        print(content)
    else:
        print("File Content:\n")
        print(content)
        print("\n" + "=" * 30)

if __name__ == "__main__":
    main()

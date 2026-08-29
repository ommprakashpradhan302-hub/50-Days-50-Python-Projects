# Student Grade Calculator
def calculate_grade(marks):
    total = sum(marks)
    count = len(marks)
    percentage = (total / (count * 100)) * 100

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return total, percentage, grade

def main():
    print("=== STUDENT GRADE CALCULATOR ===")
    n = int(input("Enter number of subjects: "))
    subjects = []
    marks = []

    for i in range(n):
        subject = input(f"Enter subject {i+1} name: ")
        mark = float(input(f"Enter marks for {subject} (out of 100): "))
        subjects.append(subject)
        marks.append(mark)

    total, percentage, grade = calculate_grade(marks)

    print("\n=== RESULT ===")
    print(f"Total Marks: {total} out of {(n*100)}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()

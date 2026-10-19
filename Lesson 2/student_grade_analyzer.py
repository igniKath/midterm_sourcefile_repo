"""Student Grade Analyzer - Starter Code

Complete every section marked TODO. Keep this file and grades.txt in the
same folder. Rename the completed file to student_grade_analyzer_.py.
"""


def classify_grade(grade):
    """Return the classification and status of a grade."""
    if grade >= 90:
        return "Excellent", "Passed"
    elif grade >= 85:
        return "Very Good", "Passed"
    elif grade >= 80:
        return "Good", "Passed"
    elif grade >= 75:
        return "Satisfactory", "Passed"
    else:
        return "Needs Improvement", "Failed"


def load_students(filename):
    """Read valid student records from a text file and return them as a list."""
    students = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line or line.startswith("#"):
                    continue

                parts = [part.strip() for part in line.split(",")]

                if len(parts) != 3:
                    continue

                student_id, name, grade_text = parts

                if not student_id or not name:
                    continue

                try:
                    grade = float(grade_text)
                    if grade < 0 or grade > 100:
                        continue
                except ValueError:
                    continue

                students.append({
                    "student_id": student_id,
                    "name": name,
                    "grade": grade,
                })
    except FileNotFoundError:
        print("Error: The file is not found.")

    return students


def calculate_statistics(students):
    """Calculate and return the class statistics."""
    if not students:
        return None

    total_grade = 0
    passed_count = 0
    failed_count = 0
    highest_student = students[0]
    lowest_student = students[0]

    for student in students:
        grade = student["grade"]
        total_grade += grade

        _, status = classify_grade(grade)
        if status == "Passed":
            passed_count += 1
        else:
            failed_count += 1

        if grade > highest_student["grade"]:
            highest_student = student

        if grade < lowest_student["grade"]:
            lowest_student = student

    average = total_grade / len(students)

    return {
        "total_students": len(students),
        "average_grade": average,
        "highest_grade": highest_student["grade"],
        "lowest_grade": lowest_student["grade"],
        "passed_count": passed_count,
        "failed_count": failed_count,
        "highest_student": highest_student["name"],
        "lowest_student": lowest_student["name"],
    }


def display_students(students):
    """Display all student records in a formatted table."""
    print(f"{'Student ID':<12}{'Name':<20}{'Grade':<7}{'Classification':<15}{'Status':<8}")
    print("-" * 70)

    for student in students:
        classification, status = classify_grade(student["grade"])
        print(f"{student['student_id']:<12}{student['name']:<20}{student['grade']:<7}{classification:<15}{status:<8}")


def display_statistics(statistics):
    """Display the calculated class statistics."""
    if not statistics:
        print("No statistics available.")
        return

    print("\nCLASS STATISTICS")
    print(f"Total Students: {statistics['total_students']}")
    print(f"Average Grade: {statistics['average_grade']:.2f}")
    print(f"Highest Grade: {statistics['highest_grade']:.2f} ({statistics['highest_student']})")
    print(f"Lowest Grade: {statistics['lowest_grade']:.2f} ({statistics['lowest_student']})")
    print(f"Passed: {statistics['passed_count']}")
    print(f"Failed: {statistics['failed_count']}")


def search_student(students, keyword):
    """Return records whose student number or name matches the keyword."""
    matches = []

    cleaned_keyword = keyword.strip().lower()
    if not cleaned_keyword:
        return matches

    for student in students:
        if cleaned_keyword in student["student_id"].lower() or cleaned_keyword in student["name"].lower():
            matches.append(student)

    return matches


def save_report(students, statistics, filename):
    """Write the student results and class statistics to a report file."""
    try:
        with open(filename, "w", encoding="utf-8") as report_file:
            report_file.write("STUDENT GRADE REPORT\n")
            report_file.write("======================\n\n")
            report_file.write(f"{'Student ID':<12}{'Name':<20}{'Grade':<7}{'Classification':<15}{'Status':<8}\n")
            report_file.write("-" * 70 + "\n")

            for student in students:
                classification, status = classify_grade(student["grade"])
                report_file.write(f"{student['student_id']:<12}{student['name']:<20}{student['grade']:<7}{classification:<15}{status:<8}\n")

            report_file.write("\nCLASS STATISTICS\n")
            report_file.write("---------------\n")

            if statistics:
                report_file.write(f"Total Students: {statistics['total_students']}\n")
                report_file.write(f"Average Grade: {statistics['average_grade']:.2f}\n")
                report_file.write(f"Highest Grade: {statistics['highest_grade']:.2f} ({statistics['highest_student']})\n")
                report_file.write(f"Lowest Grade: {statistics['lowest_grade']:.2f} ({statistics['lowest_student']})\n")
                report_file.write(f"Passed: {statistics['passed_count']}\n")
                report_file.write(f"Failed: {statistics['failed_count']}\n")
    except OSError:
        print(f"Error: Could not write the report to {filename}.")
        return False

    return True


def main():
    """Run the menu-driven Student Grade Analyzer."""
    students = load_students("grades.txt")

    if not students:
        print("No valid student records were loaded.")
        return

    statistics = calculate_statistics(students)

    while True:
        print("\nSTUDENT GRADE ANALYZER")
        print("[1] Display all students")
        print("[2] Display class statistics")
        print("[3] Search for a student")
        print("[4] Save report")
        print("[5] Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_students(students)
        elif choice == "2":
            display_statistics(statistics)
        elif choice == "3":
            keyword = input("Enter student ID or name: ").strip()
            matches = search_student(students, keyword)
            if not matches:
                print("No matching students found.")
            else:
                display_students(matches)
        elif choice == "4":
            filename = input("Enter report filename: ").strip() or "student_report.txt"
            if save_report(students, statistics, filename):
                print(f"Report saved to {filename}.")
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")
            continue


if __name__ == "__main__":
    main()


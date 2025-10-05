import os

# Custom exception for invalid grades
class InvalidGradeError(Exception):
    def __init__(self, student_name, grade):
        super().__init__(f"Invalid grade '{grade}' for student: {student_name}")

def create_sample_file(filename):
    """Creates a sample student records file if it doesn't exist."""
    sample_data = """Alice, 85
Bob, 90
Charlie, 75
Dave, 82
Eve, 95
Frank, 78
Grace, Invalid Grade
"""
    with open(filename, 'w') as file:
        file.write(sample_data)
    print(f"📄 '{filename}' not found — created a sample file with sample data.\n")

def calculate_average_grade(filename):
    total = 0
    count = 0

    # Check if file exists, if not — create it
    if not os.path.exists(filename):
        create_sample_file(filename)

    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                try:
                    name, grade = line.split(',')
                    name = name.strip()
                    grade = grade.strip()

                    # Validate grade
                    if not grade.isdigit():
                        raise InvalidGradeError(name, grade)

                    total += int(grade)
                    count += 1

                except InvalidGradeError as e:
                    print(f"⚠️ {e}")
                except ValueError:
                    print(f"⚠️ Invalid line format: '{line}'")

        if count == 0:
            print("No valid student records found.")
            return

        average = total / count
        print(f"\n✅ Average Grade of {count} students: {average:.2f}")

    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the program
calculate_average_grade("student records.txt")

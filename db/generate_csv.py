import csv
import random
from faker import Faker
def generate_csv(num_rows, *subjects):
    """
    Generates a CSV file with random student names, marks for subjects, and calculated grades.

    Args:
        num_rows (int): Number of rows to generate in the CSV file.
        *subjects: Variable length argument to pass subject names.

    Returns:
        str: Name of the generated CSV file.
    """
    
    # Create a Faker object
    fake = Faker()

    # Generate a unique file name for the CSV file
    file_name = f"generated_csv_{num_rows}_rows.csv"
    
    # Write the rows to the CSV file
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        
        # Write the header row with subject names
        header = ['Student Name'] + list(subjects) + ['Grade']
        writer.writerow(header)
        
        # Generate random data for each row
        for _ in range(num_rows):
            # Generate a random student name
            student_name = fake.name()
            
            # Generate random marks for each subject
            marks = [random.randint(0, 100) for _ in subjects]
            
            # Calculate the grade based on marks
            grade = calculate_grade(sum(marks) / len(marks))
            
            # Write the row to the CSV file
            row = [student_name] + marks + [grade]
            writer.writerow(row)
            
    print(f"CSV file '{file_name}' generated successfully!")
    
    return file_name

def calculate_grade(average_mark):
    """
    Calculates the grade based on the average mark.

    Args:
        average_mark (float): Average mark of a student.

    Returns:
        str: Grade (A to F) based on the average mark.
    """
    
    # Define grade thresholds
    grade_thresholds = {
        'A': 90,
        'B': 80,
        'C': 70,
        'D': 60,
        'E': 50
    }   

    # Calculate the grade based on the average mark
    for grade, threshold in grade_thresholds.items():
        if average_mark >= threshold:
            return grade
    
    return 'F'
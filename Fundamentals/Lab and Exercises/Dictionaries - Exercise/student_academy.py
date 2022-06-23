# Write a program that keeps the information about students and their grades. 
# On the first line, you will receive an integer number representing the next pair of rows. 
# On the next lines, you will be receiving each student's name and their grade. 
# Keep track of all grades for each student and keep only the students with an average grade higher than or equal to 4.50.
# Print the final dictionary with students and their average grade in the following format:
# "{name} -> {averageGrade}"
# Format the average grade to the 2nd decimal place.

def get_average_grade(current):
    for x in current:
        result = sum(current) / len(current)
        return result


def only_above_average():
    for current_student in grades:
        average = 4.50
        if get_average_grade(grades[current_student]) >= average:
            student_average = get_average_grade(grades[current_student])
            print(f"{current_student} -> {student_average:.2f}")


grades = dict()

students_number = int(input())

for student in range(students_number):
    name = input()
    grade = float(input())
    if name not in grades:
        grades[name] = []
        grades[name].append(grade)
    else:
        grades[name].append(grade)

only_above_average()




# Write a program that reads students' names and their grades and adds them to the student record.
# On the first line, you will receive the number of students – N. On the following N lines, you will be receiving a student's name and their grade.
# For each student print all his/her grades and finally his/her average grade, formatted to the second decimal point in the format: 
#   "{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".
# The order in which we print the result does not matter.

students_grades = int(input())

students = dict()

for _ in range(students_grades):
    name, grade_str = input().split()
    grade = float(grade_str)
    if name not in students:
        students[name] = []
    students[name].append(grade)

for current_student in students.items():
    student, grades = current_student[0], current_student[1]
    print(f"{student} ->",' '.join([f"{x:.2f}" for x in grades]), f"(avg: {sum(grades) / len(grades):.2f})")


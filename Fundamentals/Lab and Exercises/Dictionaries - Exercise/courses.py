# Write a program that keeps the information about courses. Each course has a name and registered students.
# You will be receiving a course name and a student name until you receive the command "end". 
# You should register each user into the corresponding course. If the given course does not exist, add it. 
# When you receive the command "end", print the courses with their names and total registered users. For each course, print the registered users.


registered_users = dict()

cmd = input()

while not cmd == "end":
    course, student = cmd.split(" : ")
    if course not in registered_users:
        registered_users[course] = []
        registered_users[course].append(student)
    else:
        registered_users[course].append(student)
    cmd = input()

for course in registered_users:
    print(f"{course}: {len(registered_users[course])}")
    for el in registered_users[course]:
        print(f"-- {el}")

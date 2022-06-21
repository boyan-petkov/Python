# You will be receiving names of students, their ID, and a course of programming they have taken in the format "{name}:{ID}:{course}".
# On the last line, you will receive a name of a course in snake case lowercase letters. 
# You should print only the information of the students who have taken the corresponding course in the format: "{name} - {ID}" on separate lines. 


all_courses = dict()

cmd = input()
searched = ""
while True:
    cmd = cmd.split(":")
    if len(cmd) == 3:
        name, id, course = cmd[0], cmd[1], cmd[2]
        if course not in all_courses:
            all_courses[course] = {}
            all_courses[course][id] = name
        else:
            all_courses[course][id] = name
    else:
        break
    cmd = input()
    searched = cmd

searched = searched.split("_")
final = " ".join(searched)

if final in all_courses:
    for id, name in all_courses[final].items():
        print(f"{name} - {id}")
        

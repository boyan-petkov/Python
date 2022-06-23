# The force users struggle to remember which side is the different force users from because they switch them too often.
# So you are tasked to create a web application to manage their profiles. You should store information for every unique force user registered in the application.
# You will receive several input lines in one of the following formats:
# "{force_side} | {force_user}"
# "{force_user} -> {force_side}"
# The "force_user" and "force_side" are strings, containing any character. 
# If you receive "force_side | force_user":
# •	If there is no such force user and no such force side -> create a new force side and add the force user to the corresponding side.
# •	Only if there is no such force user in any force side -> add the force user to the corresponding side. 
# •	If there is such force user already -> skip the command and continue to the next operation.
# If you receive a "force_user -> force_side":
# •	If there is such force user already -> change their side. 
# •	If there is no such force user in any force side -> add the force user to the corresponding force side.
# •	If there is no such force user and no such force side -> create new force side and add the force user to the corresponding side.
# •	Then you should print on the console: "{force_user} joins the {force_side} side!".
# You should end your program when you receive the command "Lumpawaroo". At that point, you should print each force side. For each side, print the force users.
# In case there are no force users on a side, you shouldn't print the side information. 
# Input / Constraints
# •	The input comes in the form of commands in one of the formats specified above.
# •	The input ends when you receive the command "Lumpawaroo".

def add_and_sum(language_dict, current_language):
    if current_language not in language_dict:
        language_dict[current_language] = 1
    else:
        language_dict[current_language] += 1

results = dict()
languages_used = dict()

cmd = input()

while not cmd == "exam finished":
    cmd = cmd.split("-")
    if not cmd[1] == "banned":
        name, language, points = cmd[0], cmd[1], int(cmd[2])
        add_and_sum(languages_used, language)
        if name not in results:
            results[name] = []
            results[name].append(language)
            results[name].append(points)
        elif name in results:
            if results[name][1] < points:
                results[name][1] = points
    else:
        name = cmd[0]
        del results[name]
    cmd = input()

print("Results:")
for user, points in results.items():
    print(f"{user} | {results[user][1]}")
print("Submissions:")
for language, number_of_people in languages_used.items():
    print(f"{language} - {number_of_people}")

# Here comes the final and the most interesting part – the Final ranking of the candidate-interns. 
# The final ranking is determined by the points of the interview tasks and by the points from the exams in SoftUni. Here is your final task. 
# You will receive some lines of input in the format "{contest}:{password for contest}" until you receive "end of contests". 
# Save that data because you will need it later. 
# After that you will receive other type of inputs in format "{contest}=>{password}=>{username}=>{points}" until you receive "end of submissions". 
# Here is what you need to do.
# •	Check if the contest is valid (It is considered valid if you received it in the first type of input)
# •	Check if the password is correct for the given contest
# •	If the contest and the password is valid, save the user with the contest they take part in (a user can take part in many contests) and 
# the points the user has in the given contest. If you receive the same contest and the same user update the points only if the new ones are more than the older ones.
# In the end, you should print the info for the user with the most points (total points for all contents they participated in) in the format "Best candidate is {user} with total {total_points} points.". After that print all students ordered by their names. For each user print each contest with the points in descending order. See the examples.

# Output
# •	On the first line, print the best user in format "Best candidate is {user} with total {total points} points.".
# •	Then print all students ordered as mentioned above in format:
# "{user_name1}
# #  {contest1} -> {points}
# #  {contest2} -> {points} 
# …
# #  {contestN} -> {points}"


contest_and_password = dict()

all_submissions = dict()
participants = []
command = input()
while not command == "end of contests":
    valid_contest, password_contest = command.split(":")
    contest_and_password[valid_contest] = password_contest
    command = input()

cmd = input()
while not cmd == "end of submissions":
    contest, password, username, points = cmd.split("=>")
    points = int(points)
    if contest in contest_and_password and contest_and_password[contest] == password:
        if username not in participants:
            participants.append(username)
        if contest not in all_submissions:
            all_submissions[contest] = []
            all_submissions[contest].append(username)
            all_submissions[contest].append(points)
        elif contest in all_submissions:
            if username in all_submissions[contest]:
                current = all_submissions[contest].index(username)
                previous_points_index = current + 1
                if all_submissions[contest][previous_points_index] < points:
                    all_submissions[contest][previous_points_index] = points
            else:
                all_submissions[contest].append(username)
                all_submissions[contest].append(points)
    cmd = input()

best_candidate = ""
most_points = 0

for participant in participants:
    points_participant = 0
    for language in all_submissions:
        if participant in all_submissions[language]:
            i_participant = all_submissions[language].index(participant)
            i_of_points = i_participant + 1
            points_participant += all_submissions[language][i_of_points]
    if points_participant > most_points:
        most_points = points_participant
        best_candidate = participant

print(f"Best candidate is {best_candidate} with total {most_points} points.")
print("Ranking:")

participants = sorted(participants)
for participant_ in participants:
    person_contests = dict()
    for contest_ in all_submissions:
        if participant_ in all_submissions[contest_]:
            i_participant = all_submissions[contest_].index(participant_)
            i_of_points = i_participant + 1
            points_ = all_submissions[contest_][i_of_points]
            person_contests[points_] = contest_
    print(f"{participant_}")
    person_contests = dict(sorted(person_contests.items(), reverse= True))
    for key,value in person_contests.items():
        print(f"#  {value} -> {key}")

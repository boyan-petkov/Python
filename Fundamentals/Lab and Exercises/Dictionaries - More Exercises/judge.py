# You know the judge system, right?! Your job is to create a program similar to the Judge system. 
# You will receive several input lines in one of the following formats:
# "{username} -> {contest} -> {points}"
# The "contest" and "username" are strings, the given "points" will be an integer number. 
# You need to keep track of every contest and points of each user: 
# •	If the user has already participated in the contest, update their points only if the new ones are more than the older ones.
# •	Otherwise, just save the data - contest, username, and points.
# Also, you need to keep individual statistics for each user - the total points of all contests (including even points from the same contents). 
# You should end your program when you receive the command "no more time". 
# At that point you should print each contest in order of input, for each contest print the participants ordered by points in descending order, 
# then ordered by name in ascending order. After that, you should print individual statistics for every participant ordered by total points in descending order, 
# and then by alphabetical order.

# Output
# •	The output format for the contests is:
# "{constest_name}: {number_participants} participants
# 1. {username1} <::> {points}
# 2. {username2} <::> {points}
# …
# {N}. {usernameN} <::> {points}"
# •	After you print all contests, print the individual statistics for every participant.
# •	The output format is:
# "Individual standings:
# 1.	{username1} -> {total_points}
# 2.	{username} -> {total_points}


all_contests = dict()
individual_statistic = dict()
help_me = dict()

command = input()
while not command == "no more time":
    username, contest, points = command.split(" -> ")
    points = int(points)
    if username not in individual_statistic:
        individual_statistic[username] = points
        help_me[username] = {contest: points}
    elif username in individual_statistic:
        if contest in help_me[username]:
            if help_me[username][contest] < points:
                help_me[username][contest] = points
                individual_statistic[username] = points
        else:
            individual_statistic[username] += points
    if contest not in all_contests:
        all_contests[contest] = {username: points}
    elif contest in all_contests and username not in all_contests[contest]:
        all_contests[contest][username] = points
    elif contest in all_contests and username in all_contests[contest]:
        if all_contests[contest][username] < points:
            all_contests[contest][username] = points
    command = input()

for current in all_contests:
    print(f"{current}: {len(all_contests[current])} participants")
    sort = dict(sorted(all_contests[current].items(), key=lambda item: (-item[1], item[0])))
    # сортиране първо по точките след това по име
    num = 0
    for name, current_points in sort.items():
        num += 1
        print(f"{num}. {name} <::> {current_points}")
print("Individual standings:")
num = 0
sort_names = dict(sorted(individual_statistic.items(), key=lambda item: (-item[1], item[0])))
for current_user, points in sort_names.items():
    num += 1
    print(f"{num}. {current_user} -> {points}")

# You are a pro MOBA player, you are struggling to become а master of the Challenger tier. So, you carefully watch the statistics in the tier.
# You will receive several input lines in one of the following formats:
# "{player} -> {position} -> {skill}"
# "{player} vs {player}"
# The "player" and "position" are strings, and the given "skill" will be an integer number. You need to keep track of every player.
# When you receive a player with his position and skill, add him to the players' pool, 
# if he isn`t present, else add his position and skill or update his skill, only if the current position skill is lower than the new value.
# If you receive "{player} vs {player}" and both players exist in the tier, they duel with the following rules:
# •	If they got at least one position in common, the player with better total skill points wins and the other is demoted from the tier -> remove him. 
# •	If they have same total skill points at the same positions, the duel is tie and they both continue in the Season.
# •	If they don`t have positions in common, the duel isn`t happening and both continue in the Season.
# You should end your program when you receive the command "Season end". 
# At that point you should print the players, ordered by total skill in descending order, then ordered by player name in ascending order. 
# For each player print their position and skill, ordered descending by skill, then ordered by position name in ascending order.

# Output
# •	The output format for each player is:
# "{player}: {total_skills} skill"
# - {position1} <::> {skill}
# - {position2} <::> {skill}


def sum_skills(some_dict):
    total = 0
    for values in some_dict.values():
        total += values
    return total

def compare(dict1, dict2):
    for key in dict1:
        if key in dict2:
            return True

players_pool = dict()

command = input()
while not command == "Season end":
    if "->" in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)
        if player not in players_pool:
            players_pool[player] = {position: skill}
        elif player in players_pool and position in players_pool[player]:
            if players_pool[player][position] < skill:
                players_pool[player][position] = skill
        elif player in players_pool and position not in players_pool[player]:
            players_pool[player][position] = skill
    elif " vs " in command:
        player1, player2 = command.split(" vs ")
        if player1 in players_pool and player2 in players_pool:
            if compare(players_pool[player1], players_pool[player2]):
                player1_skills = sum_skills(players_pool[player1])
                player2_skills = sum_skills((players_pool[player2]))
                if player1_skills > player2_skills:
                    del players_pool[player2]
                elif player2_skills > player1_skills:
                    del players_pool[player1]
                else:
                    continue
    command = input()

sorted_names = dict(sorted(players_pool.items(), key=lambda x: (-sum(x[1].values()), x[0])))

for k, v in sorted_names.items():
    current = k
    print(f"{k}: {sum(v.values())} skill")
    sorted_skills = (sorted(sorted_names[current].items(), key=lambda x: (-x[1], x[0])))
    for item in sorted_skills:
        print(f"- {item[0]} <::> {item[1]}")



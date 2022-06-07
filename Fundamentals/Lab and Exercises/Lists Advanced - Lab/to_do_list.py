# You will be receiving to-do notes until you get the command "End". The notes will be in the format: "{importance}-{note}". 
# Return a list containing all to-do notes sorted by importance in ascending order. 
# The importance value will always be an integer between 1 and 10 (inclusive).

to_do = ["" for i in range(11)]

command = input()
while not command == "End":
    command = command.split("-")
    priority, note = int(command[0]), (command[1])
    to_do[priority] = note
    command = input()

final = [el for el in to_do if not el == ""]
print(final)

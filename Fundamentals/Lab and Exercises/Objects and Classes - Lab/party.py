# Create a class Party that only has an attribute people – empty list. The __init__ method should not accept any parameters. 
# You will be given names of people (on separate lines) until you receive the command "End". Use the created class to solve this problem. 
# After you receive the "End" command, print 2 lines:
# •	"Going: {people}" - the people should be separated by comma and space ", ".
# •	"Total: {total_people_going}"
# Note: submit all of your code, including the class



class Party:
    def __init__(self):
        self.people = []


party = Party()

command = input()
while not command == "End":
    party.people.append(command)
    command = input()


total_people_going = len(party.people)
print(f"Going: {', '.join(party.people)}")
print(f"Total: {total_people_going}")

# Input
# Peter
# John
# Katy

# Input2
# Sam
# Eddy
# Edd
# Kris
# End

# You will receive a number representing the number of wagons a train has. Create a list (train) with the given length containing only zeros. 
# Until you receive the command "End", you will receive some of the following commands:
# •	"add {people}" – you should add the number of people in the last wagon
# •	"insert {index} {people}" - you should add the number of people at the given wagon
# •	"leave {index} {people}" - you should remove the number of people from the wagon. 
# There will be no case in which the people will be more than the count in the wagon.
# There will be no case in which the index is invalid!
# After you receive the "End" command print the train.

wagons = int(input())

train = []

for num in range(wagons):
    train.append(int(0))

command = input()
while not command == "End":
    command = command.split()
    cmd = command[0]
    if cmd == "add":
        last = len(train) - 1
        train[last] += int(command[1])
    elif cmd == "insert":
        index = int(command[1])
        value = int(command[2])
        train[index] += value
    elif cmd == "leave":
        index = int(command[1])
        value = int(command[2])
        train[index] -= value
    command = input()

print(train)

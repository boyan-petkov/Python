# Tom is working at the supermarket, and he needs your help to keep track of his clients. 
# Write a program which reads lines of input consisting of a customer's name and adds it to the end of a queue until "End" is received. 
# If in a meantime you receive the command "Paid", you should print each customer in the order they are served (from the first to the last one) and empty the queue. 
# When you receive "End", you should print the count of the remaining people in the queue in the format: "{count} people remaining.".

from collections import deque

clients = deque()

command = input()
while not command == "End":
    if command == "Paid":
        for i in range(len(clients)):
            print(clients.popleft())
    else:
        clients.append(command)
    command = input()
print(f"{len(clients)} people remaining.")

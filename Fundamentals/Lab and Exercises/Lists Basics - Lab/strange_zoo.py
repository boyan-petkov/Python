# You are at the zoo, and the meerkats look strange. 
# You will receive 3 strings on separate lines, representing the tail, the body, and the head of an animal in that order. 
# Your task is to re-arrange the elements in a list so that the animal looks normal again:
# •	On the first position is the head;
# •	On the second position is the body;
# •	On the last one is the tail.


zoo = []

for el in range(3):
    zoo.append(input())
    
zoo[0], zoo[2] = zoo[2], zoo[0]

print(zoo)

# You are a facility manager at a large business center. 
# One of your responsibilities is to check if each conference room in the center has enough chairs for the visitors.
# On the first line, you will be given an integer n representing the number of rooms in the business center. 
# On the following n lines for each room, you will receive information about the chairs in the room and the number of visitors.
# Each chair will be presented with the char "X". Next, there will be a single space and the number of visitors at the end. 
# For example: "XXXXX 4" (5 chairs and 4 visitors). 
# Keep track of the free chairs:
# •	If there are not enough chairs in a specific room, print the following message: 
#   "{needed_chairs_in_room} more chairs needed in room {number_of_room}". The rooms start from 1.
# •	Otherwise, print: "Game On, {total_free_chairs} free chairs left".

rooms = int(input())
chairs_enough = True
free_chair = 0
for room in range(rooms):
    chairs, people = input().split()
    current_room = room + 1
    if len(chairs) < int(people):
        print(f"{abs(len(chairs) - int(people))} more chairs needed in room {current_room}")
        chairs_enough = False
    else:
        free_chair += len(chairs) - int(people)
if chairs_enough:
    print(f"Game On, {free_chair} free chairs left")




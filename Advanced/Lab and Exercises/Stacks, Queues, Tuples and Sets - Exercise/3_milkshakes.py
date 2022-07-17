# You are learning how to make milkshakes.
# First, you will be given two sequences of integers representing chocolates and cups of milk.
# You have to start from the last chocolate and try to match it with the first cup of milk. 
# If their values are equal, you should make a milkshake and remove both ingredients. 
# Otherwise, you should move the cup of milk at the end of the sequence and decrease the value of the chocolate by 5 without moving it from its position.
# If any of the values are equal to or below 0, you should remove them from the records right before mixing them with the other ingredient.
# When you successfully prepare 5 chocolate milkshakes, or you have no more chocolate or cups of milk left, you need to stop making chocolate milkshakes.

# Input
# •	On the first line of input, you will receive the integers representing the chocolate, separated by  ", ". 
# •	On the second line of input, you will receive the integers representing the cups of milk, separated by ", ".

# Output
# •	On the first line, print:
# o	If you successfully made 5 milkshakes: "Great! You made all the chocolate milkshakes needed!"
# o	Otherwise: "Not enough milkshakes."
# •	On the second line - print:
# o	If there are chocolates left: "Chocolate: {chocolate1}, {chocolate2}, (…)"
# o	Otherwise: "Chocolate: empty"
# •	On the third line - print:
# o	If there are cups of milk left: "Milk: {milk1}, {milk2}, {milk3}, (…)"
# o	Otherwise: "Milk: empty"
  
# Constraints
# •	All given numbers will be valid integers in the range [-100 … 100].

from collections import deque


def print_leftovers(collection, degredient):
    if len(collection) > 0:
        print(f"{degredient}: " + ', '.join([str(x) for x in collection]))
    else:
        print(f"{degredient}: empty")


chocolates = deque([int(x) for x in input().split(", ")])
cups = deque([int(x) for x in input().split(", ")])

milkshakes = 0
completed = False

while chocolates and cups and milkshakes < 5:
    chocolate, milk = chocolates.pop(), cups.popleft()
    if chocolate <= 0 and milk <= 0:
        continue
    
    if chocolate <= 0:
        cups.appendleft(milk)
        continue
        
    if milk <= 0:
        chocolates.append(chocolate)
        continue
        
    if chocolate == milk:
        milkshakes += 1

    else:
        cups.append(milk)
        choc = chocolate - 5
        chocolates.append(choc)
    if milkshakes == 5:
        completed = True
        break
if completed:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
print_leftovers(chocolates, "Chocolate")
print_leftovers(cups, "Milk")

# On the first line, you will receive a single number n. On the following n lines, you will receive integers. 
# After that, you will be given one of the following commands:
# •	even
# •	odd
# •	negative
# •	positive
# Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.


number = int(input())

even = []
odd = []
negative = []
positive = []
decision = ""

for _ in range(number):
    current_num = int(input())
    if current_num % 2 == 0 or current_num == 0:
        even.append(current_num)
    if current_num % 2 != 0:
        odd.append(current_num)
    if current_num >= 0:
        positive.append(current_num)
    if current_num < 0:
        negative.append(current_num)
command = input()
if command == "even":
    decision = even
elif command == "odd":
    decision = odd
elif command == "positive":
    decision = positive
else:
    decision = negative
print(decision)

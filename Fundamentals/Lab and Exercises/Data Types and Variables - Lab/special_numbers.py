# # Write a program that reads an integer n. Then, for all numbers in the range [1, n], prints the number and if it is special or not (True / False). 
# A number is special when the sum of its digits is 5, 7, or 11.

number = int(input())

for num in range(1, number + 1):
    number_as_string = str(num)
    result = 0
    for symbol in range(len(number_as_string)):
        result += int(number_as_string[symbol])
    if result == 5 or result == 7 or result == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")

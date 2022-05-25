# Write a program that receives two numbers (factor and count). It should create a list with a length of the given count that contains only integer numbers, 
# which are multiples of the given factor. 
# The numbers should be only positive, and they should be arranged in ascending order, starting from the value of the factor.

import sys

factor = int(input())

count = int(input())

list = []

for digit in range(1, sys.maxsize):
    if digit % factor == 0:
        list.append(digit)
    if len(list) == count:
        break
print(list)

# Write a program which reads from the console a string with N integers, separated by a single space, and reverses them using a stack. 
# Print the reversed integers on one line, separated by a single space.

from collections import deque

nums = deque(input().split())

while nums:
    print(nums.pop(), end=" ")

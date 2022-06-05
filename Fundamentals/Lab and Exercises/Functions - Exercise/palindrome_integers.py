# A palindrome is a number that reads the same backward as forward, such as 323 or 1001.
# Write a function that receives a list of positive integers, separated by comma and space ", ". 
# The function should check if each integer is a palindrome - True or False. Print the result.

def is_palindrome(nums):
    for el in nums:
        if el == el[:: -1]:
            print(True)
        else:
            print(False)


numbers = [el for el in input().split(", ")]
is_palindrome(numbers)

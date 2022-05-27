# Write a program that receives a list of integer numbers (separated by a single space) and a number n. 
# The number n represents the count of numbers to remove from the list. 
# You should remove the smallest ones, and then, you should print all the numbers that are left in the list, separated by a comma and a space ", ".


num_input = input().split()

nums = [int(num) for num in num_input]

remove = int(input())

for el in range(remove):
    nums.remove(min(nums))
nums = list(map(lambda x: str(x), nums))


print(", ".join(nums))

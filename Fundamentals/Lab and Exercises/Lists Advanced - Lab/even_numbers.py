# Write a program that reads a single string with numbers separated by comma and space ", ". Print the indices of all even numbers.

nums = [int(el) for el in input().split(", ")]

indexes = []
for i in range(len(nums)):
        if nums[i] % 2 == 0:
            indexes.append(i)

print(indexes)

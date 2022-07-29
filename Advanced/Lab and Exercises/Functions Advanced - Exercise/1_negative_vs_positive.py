# You will receive a sequence of numbers (integers) separated by a single space. Separate the negative numbers from the positive. 
# Find the total sum of the negatives and positives, and print the following:
# On the first line, print the sum of the negatives
# On the second line, print the sum of the positives
# On the third line:
# If the absolute negative number is larger than the positive number:
# 	"The negatives are stronger than the positives"
# If the positive number is larger than the absolute negative number:
# 	"The positives are stronger than the negatives"
# Note: you will not receive any zeroes in the input.

nums = [int(x) for x in input().split()]
positive, negative = [x for x in nums if x > 0], [x for x in nums if x < 0]

print(sum(negative))
print(sum(positive))
if sum(positive) > abs(sum(negative)):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")

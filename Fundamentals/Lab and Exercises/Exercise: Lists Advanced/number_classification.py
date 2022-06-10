# Using comprehension, write a program that receives some text, separated by space, and take only those words whose length is even. 
# Print each word on a new line.

nums = list(map(int, input().split(", ")))

positive, negative, even, odd = [], [], [], []

for num in nums:
    if num >= 0:
        positive.append(num)
    if num % 2 == 0:
        even.append(num)
    if num < 0 :
        negative.append(num)
    if num % 2 != 0:
        odd.append(num)
positive = list(map(str, positive))
negative = list(map(str, negative))
even = list(map(str, even))
odd = list(map(str, odd))

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")

# On the first line, you will receive a number n. On the following n lines, you will receive integers. 
# You should create and print two lists:
# •	One with all the positives (including 0) numbers
# •	One with all the negatives numbers
# Finally, print the following message: 
# "Count of positives: {count_positives}
# Sum of negatives: {sum_of_negatives}"

number = int(input())

positives = []
negatives = []

for _ in range(number):
    current = int(input())
    if current >= 0:
        positives.append(current)
    else:
        negatives.append(current)

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum(negatives)}")

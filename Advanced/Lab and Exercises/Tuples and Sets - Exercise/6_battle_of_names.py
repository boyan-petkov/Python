# You will receive a number N. On the next N lines, you will be receiving names. 
# You must sum the ascii values of each letter in the name and integer divide it to the number of the current row (starting from 1). 
# Save the result to a set of either odd or even numbers, depending on if the devised number is an odd or even. After that, sum the values of each set.
# •	If the sums of the two sets are equal, print the union of the values, separated by ", ". 
# •	If the sum of the odd numbers is bigger than the sum of the even numbers, print the different values, separated by ", ".
# •	If the sum of the even numbers is bigger than the sum of the odd numbers, print the symmetric different values, separated by ", ".
# NOTE: On every operation, the starting set should be the odd set


lines_num = int(input())

odd_set = set()
even_set = set()

even_sum = 0
odd_sum = 0

for current_row in range(1, lines_num + 1):
    name = [ord(x) for x in input()]
    name_value = sum(name) // current_row
    if name_value % 2 == 0:
        even_set.add(name_value)
        even_sum += name_value
    else:
        odd_set.add(name_value)
        odd_sum += name_value
result = set()
if even_sum == odd_sum:
    result = even_set.union(odd_set)
elif odd_sum > even_sum:
    result = odd_set.difference(even_set)
elif even_sum > odd_sum:
    result = even_set.symmetric_difference(odd_set)
print(", ".join([str(x) for x in result ]))




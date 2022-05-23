# Write a program, which sums the ASCII codes of N characters and prints the sum on the console. 
# On the first line, you will receive N – the number of lines. On the following N lines – you will receive a letter per line. 
# Print the total sum in the following format: "The sum equals: {total_sum}".
# Note: n will be in the interval [1…20].

lines = int(input())

result = 0
for _ in range (lines):
    char = input()
    result += ord(char)

print(f"The sum equals: {result}")

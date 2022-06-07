# On the first line, you will receive words separated by a single space. On the second line, you will receive a palindrome. 
# First, you should print a list containing all the found palindromes in the sequence. 
# Then, you should print the number of occurrences of the given palindrome in the format: "Found palindrome {number} times".

words = [el for el in input().split()]

palindromes = [el for el in words if el == el[::-1]]

searched = input()

count = 0

for i in range(len(palindromes)):
    if searched == palindromes[i]:
        count += 1

print(palindromes)
print(f"Found palindrome {count} times")

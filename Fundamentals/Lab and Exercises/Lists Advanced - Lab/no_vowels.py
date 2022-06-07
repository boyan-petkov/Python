# Using comprehension, write a program that receives a text and removes all its vowels, case insensitive. 
# Print the new text string after removing the vowels. The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'.

vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']

text = input()
string = [el for el in text if el not in vowels]

print("".join(string))

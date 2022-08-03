# Write a function words_sorting which receives a different number of words.
# Create a dictionary, which will have as keys the words that the function received. 
# For each key, create a value that is the sum of all ASCII values of that key.
# Then, sort the dictionary:
# •	By values in descending order, if the sum of all values of the dictionary is odd
# •	By keys in ascending order, if the sum of all values of the dictionary is even
# Note: Submit only the function in the judge system
  
# Input
# •	There will be no input, just any number of words passed to your function

# Output
# •	The function should return a string in the format "{key} - {value}" for each key and value on a separate lines
# Constraints:
# •	There will be no case with capital letters.
# •	There will be no case with a string consisting of other than letters.

def words_sorting(*args):
    result = ""
    total = 0
    for word in args:
        value = 0
        for char in word:
            value += ord(char)
        final_dict[word] = value
        total += value


    if total % 2 == 0:
        sorted_dic = sorted(final_dict.items(), key=lambda x: x[0])
    else:
        sorted_dic = sorted(final_dict.items(), key=lambda x: (-x[1]))
    for kvp in sorted_dic:
        result += f"{kvp[0]} - {kvp[1]}\n"
    return result



final_dict = {}

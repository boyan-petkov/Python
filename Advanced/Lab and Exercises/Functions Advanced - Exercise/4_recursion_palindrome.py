# Write a recursive function called palindrome() that will receive a word and an index (always 0). 
# Implement the function, so it returns "{word} is a palindrome" if the word is a palindrome and "{word} is not a palindrome" 
# if the word is not a palindrome using recursion. Submit only the function in the judge system.


def palindrome(*args):
    text, idx = args[0], int(args[1])
    if idx == len(text) // 2:
        return f"{text} is a palindrome"

    left = text[idx]
    right = text[len(text) - 1 - idx]
    
    if left != right:
        return f"{text} is not a palindrome"

    return palindrome(text, idx + 1)


print(palindrome("peter", 0))
print(palindrome("abcba", 0))

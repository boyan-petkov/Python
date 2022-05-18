from math import floor
 
word = input()
 
best_score = 0
most_powerful = ""
 
while word != "End of words":
    vowel = False
    current_score = 0
    for letter in word[0]:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" \
                or letter == "y" or letter == "A" or letter == "E" or letter == "I" \
                or letter == "O" or letter == "U" or letter == "Y":
            vowel = True
    for every_letter in word:
        current_score += ord(every_letter)
    if vowel:
        current_score *= len(word)
    else:
        current_score = floor(current_score / len(word))
    if current_score > best_score:
        best_score = current_score
        most_powerful = word
    word = input()
print(f"The most powerful word is {most_powerful} - {best_score}")

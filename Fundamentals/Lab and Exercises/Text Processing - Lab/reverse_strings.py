# You will be given series of strings until you receive an "end" command. 
# Write a program that reverses strings and prints each pair on separate line in the format "{word} = {reversed word}".


word = input()

while not word == "end":
    word_reverse = reversed(word)
    word_reverse = "".join(word_reverse)
    print(f"{word} = {word_reverse}")



    word = input()

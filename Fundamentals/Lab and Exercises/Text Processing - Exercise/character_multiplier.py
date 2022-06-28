# Create a program that receives two strings on a single line separated by a single space. 
# Then, it prints the sum of their multiplied character codes as follows: multiply str1[0] with str2[0] and add the result to the total sum, 
# then continue with the next two characters. 
# If one of the strings is longer than the other, add the remaining character codes to the total sum without multiplication.

def sum_func(firs_word, second_word):
    total_sum = 0

    for i in range(len(firs_word)):
        if i < len(second_word):
            total_sum += ord(firs_word[i]) * ord(second_word[i])

        else:
            total_sum += ord(firs_word[i])
    return total_sum


def char_multiply(first_word, second_word):
    result = 0
    if len(first_word) > len(second_word):
        result = sum_func(first_word, second_word)
    else:
        result = sum_func(second_word, first_word)
    print(result)

text  = input().split()

char_multiply(text[0], text[1])

# Write a function that receives two characters and returns a single string with all the characters 
# in between them (according to the ASCII code), separated by a single space. 
# Print the result on the console.


def chars(start, end):
    for el in range(ord(start) + 1, ord(end)):
        print(chr(el), end=" ")


first = input()
last = input()
chars(first, last)

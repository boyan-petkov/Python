# Write a program to read an integer N and print all triples of the first N small Latin letters, ordered alphabetically:

num = int(input())

for q in range(0, num):
    for  w in range(0, num):
        for e in range(0, num):
            print(f"{chr(97 + q)}{chr(97 + w)}{chr(97 + e)}")

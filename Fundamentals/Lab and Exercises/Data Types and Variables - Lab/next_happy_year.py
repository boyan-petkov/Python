# You are saying goodbye to your best friend: "See you next happy year". Happy Year is the year with only distinct digits, for example, 2018. 
#   Write a program that receives an integer number and finds the next happy year.

year = int(input())

found = False

happy_year = 0

while not found:
    year += 1
    if len(set(str(year))) == len(str(year)):
        found = True
print(year)

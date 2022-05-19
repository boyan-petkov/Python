# Write a program that receives a number n on the first line. On the following n lines, 
# it receives different integer numbers. If the program receives an odd number print "{num} is odd!" 
# and end the program. Otherwise, if all numbers given are even, print "All numbers are even.".

number = float(input())

condition = False

while not condition:
    if number < 1 or number > 100:
        number = float(input())
        continue
    condition = True
    break

print(f"The number {number} is between 1 and 100")

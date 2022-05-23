# Write a program that reads four integer numbers. It should add the first to the second number, integer divide the sum by the third number, 
# and multiply the result by the fourth number. Print the final result.

a, b, c, d, = int(input()), int(input()), int(input()), int(input()),

result = ((a + b) // c) * d
print(result)

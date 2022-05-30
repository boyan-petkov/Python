# Write a function that receives a string and a counter n. The function should return a new string – the re


repeat_string = lambda a, b: a * b

string, count = input(), int(input())

print(repeat_string(string, count))

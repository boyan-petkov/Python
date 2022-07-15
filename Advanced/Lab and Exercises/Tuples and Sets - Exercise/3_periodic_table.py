# Write a program that keeps all the unique chemical elements. 
# On the first line you will be given a number n - the count of input lines that you are going to receive. 
# On the next n lines, you will be receiving chemical compounds, separated by a single space. 
# Your task is to print all the unique ones on separate lines (the order does not matter):


number_of_inputs = int(input())
some_set = set()

for _ in range(number_of_inputs):
    current = input().split()
    some_set = some_set.union(current)
print("\n".join(some_set)) 

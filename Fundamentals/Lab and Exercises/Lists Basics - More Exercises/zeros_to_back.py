# Write a program that receives a single string (integers separated by a comma and space ", "), finds all the zeros, 
# and moves them to the back without messing up the other elements. 
# Print the resulting integer list.


integer_list = [int(x) for x in input().split(", ")]

count = 0
while 0 in integer_list:
    integer_list.remove(0)
    count += 1
for zeros in range(count):
    integer_list.append(0)

print(integer_list)


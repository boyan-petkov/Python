# You have an empty stack. You will receive an integer – N. On the next N lines you will receive queries.
# Each query is one of these four types:
# •	'1 {number}' – push the number (integer) into the stack
# •	'2' – delete the number at the top of the stack
# •	'3' – print the maximum number in the stack
# •	'4' – print the minimum number in the stack
# It is guaranteed that each query is valid.
# After you go through all the queries, print the stack from the top to the bottom in the following format:
# "{n}, {n1}, {n2}, ... {nn}"


from collections import deque


def queries(query):

    if query.startswith("1"):
        num = query.split()[1]
        stack.append(int(num))
    elif query == "2":
        if stack:
            stack.pop()
    elif query == "3":
        if stack:
            print(max(stack))
    elif query == "4":
        if stack:
            print(min(stack))


def make_them_strings(some_list):
    if stack:
        while stack:
            print_list.append(str(stack.pop()))
    return print_list

stack = deque()
lines_input = int(input())
for current in range(lines_input):
    queries(input())

print_list = list()
make_them_strings(stack)

print(", ".join(print_list))

# First, you will be given two sequences of integers values on different lines. T
# he values of the sequences are separated by a single space between them.
# Keep in mind that each sequence should contain only unique values.
# Next, you will receive a number - N. On the next N lines, you will receive one of the following commands:
# •	"Add First {numbers, separated by a space}" - add the given numbers at the end of the first sequence of numbers.
# •	"Add Second {numbers, separated by a space}" - add the given numbers at the end of the second sequence of numbers.
# •	"Remove First {numbers, separated by a space}" - remove only the numbers contained in the first sequence.
# •	"Remove Second {numbers, separated by a space}" - remove only the numbers contained in the second sequence.
# •	"Check Subset" - check if any of the given sequences are a subset of the other. If it is, print "True". Otherwise, print "False".
# In the end, print the final sequences, separated by a comma and a space ", ". The values in each sequence should be sorted in ascending order.

def cycle_add(iterable, command):
    for i in range(2, (len(command))):
        iterable.add(command[i])
    return iterable


def remove_cycle(iterable, command):
    for i in range(2, len(command)):
        iterable.discard(command[i])
    return iterable


def subset(iterable1, iterable2):
    if iterable1.issubset(iterable2) or iterable2.issubset(iterable1):
        print("True")
    else:
        print("False")


first_set = set(input().split())
second_set = set(input().split())

lines_number = int(input())

for _ in range(lines_number):
    cmd = input().split()
    current_cmd = cmd[0] + " " + cmd[1]
    if current_cmd == "Add First":
        first_set = cycle_add(first_set, cmd)
    elif current_cmd == "Add Second":
        second_set = cycle_add(second_set, cmd)
    elif current_cmd == "Remove First":
        remove_cycle(first_set, cmd)
    elif current_cmd == "Remove Second":
        remove_cycle(second_set, cmd)
    elif current_cmd == "Check Subset":
        subset(first_set, second_set)

first_set = [int(x) for x in first_set]
second_set = [int(x) for x in second_set]
print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")

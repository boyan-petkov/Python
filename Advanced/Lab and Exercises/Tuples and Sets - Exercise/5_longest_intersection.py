# Write a program which finds the longest intersection. You will be given a number N. 
# On each of the next N lines you will be given two ranges in the format: "{first_start},{first_end}-{second_start},{second_end}". 
#   You should find the intersection of these two ranges. The start and end numbers in the ranges are inclusive. 
# Finally, you should find the longest intersection of all N intersections, print the numbers that are included and its length in the format: 
#   "Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}"
# Note: in each range, there will always be intersection. If there are two equal intersections, print the first one.


def divide_them(pair1, pair2):
    start, end = [int(x)for x in pair1.split(",")]
    start_, end_, = [int(x)for x in pair2.split(",")]
    pair1 = set()
    pair2 = set()
    for num in range(start, end + 1):
        nums_pair1.add(num)
    for num in range(start_, end_ + 1):
        nums_pair2.add(num)
    return nums_pair1, nums_pair2


def is_it_larger(first, second, largest, final):
    global intersection
    global current_largest
    current_intersection = first.intersection(second)
    if len(current_intersection) > largest:
        largest = len(current_intersection)
        final = current_intersection
        intersection = final
        current_largest = largest
    return intersection, current_largest


nums_pair1 = set()
nums_pair2 = set()
intersection = []
current_largest = 0
n_lines = int(input())

for _ in range(n_lines):
    line = input().split("-")
    divide_them(line[0], line[1])
    is_it_larger(nums_pair1, nums_pair2, current_largest, intersection)
    nums_pair1.clear(), nums_pair2.clear()

print(f"Longest intersection is [{', '.join([str(x)for x in intersection])}] with length {len(intersection)}")

# On the first line, you will receive a single number n. On the following n lines, you will receive names of courses. 
# You should create a list of courses and print it.

num = int(input())

courses = []

for _ in range(num):
    courses.append(input())
print(courses)

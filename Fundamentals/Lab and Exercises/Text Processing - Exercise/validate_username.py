# Write a program that reads usernames on a single line (separated by ", ") and prints all valid usernames on separate lines. 
# A valid username:
# •	has length between 3 and 16 characters inclusive
# •	can contain only letters, numbers, hyphens, and underscores
# •	has no redundant symbols before, after, or in between

def length(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def allowed_chars(name):
    for char in name:
        if not (char.isalnum() or char == "-" or char == "_"):
            return False
    return True


def redundant(name):
    for char in name:
        if char == " ":
            return False
    return True


def is_valid(name):
    if length(name) and allowed_chars(name) and redundant(name):
        return True
    return False


usernames = input().split(", ")

for current_name in usernames:
    if is_valid(current_name):
        print(current_name)

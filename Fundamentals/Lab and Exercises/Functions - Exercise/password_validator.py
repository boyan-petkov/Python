# Write a function that checks if a given password is valid. Password validations are:
# •	It should be 6 - 10 (inclusive) characters long
# •	It should consist only of letters and digits
# •	It should have at least 2 digits 
# If a password is valid, print "Password is valid".
# Otherwise, for every unfulfilled rule, print a message:
# •	"Password must be between 6 and 10 characters"
# •	"Password must consist only of letters and digits"
# •	"Password must have at least 2 digits"


def validator(password: str):
    condition1, condition2, condition3 = False, False, False
    if not len(password) >= 6 and len(password) <= 10:
        print("Password must be between 6 and 10 characters")
    else:
        condition1 = True
    for el in password:
        if not el.isdigit() and not el.isalpha():
            print("Password must consist only of letters and digits")
            condition2 = False
            break
        else:
            condition2 = True
    count = 0
    for digit in password:
        if digit.isdigit():
            count += 1
    if count < 2:
        print("Password must have at least 2 digits")
    else:
        condition3 = True
    if condition1 and condition2 and condition3:
        print("Password is valid")


current_pass = input()
validator(current_pass)

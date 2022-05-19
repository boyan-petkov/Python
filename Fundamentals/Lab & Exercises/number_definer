# Write a program that reads a floating-point number and:
# -	prints "zero" if the number is zero
# -	prints "positive" or "negative"
# -	adds "small" if the absolute value of the number is less than 1 and it is not 0, or "large" if it exceeds 1 000 000




num = float(input())
value = ""

if num == 0:
    value = "zero"
elif num > 0:
    value = "positive"
    if num > 0 and num < 1:
        value = "small positive"
    elif num > 1000000:
        value = "large positive"
elif num < 0:
    value = "negative"
    if num < 0 and num > -1:
        value = "small negative"
    elif num < -1000000:
        value = "large negative"

print(value)

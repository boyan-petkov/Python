# Write a function that receives three integer numbers and returns the smallest. 
# Print the result on the console. Use an appropriate name for the function.


def smallest(first_num, second_num, third_num):
    if first_num < second_num and first_num < third_num:
        min_num = first_num
        return min_num
    elif second_num < first_num and second_num < third_num:
        min_num = second_num
        return min_num
    else:
        min_num = third_num
        return min_num


num1, num2, num3 = int(input()), int(input()), int(input()),

print(smallest(num1, num2, num3))

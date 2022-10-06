# Having the following code:


# def number_increment(numbers):

#     def increase():

#         # TODO: Implement

#     return increase()
  
# Complete the code so it works as expected

# print(number_increment([1, 2, 3]))	[2, 3, 4]

def number_increment(nums):
    def increase():
        res = [n + 1 for n in nums]
        return res
    return increase()


print(number_increment([1, 2, 3]))

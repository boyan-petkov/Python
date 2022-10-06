
# Having the following code:
  
# def vowel_filter(function):

#     def wrapper():

#         # TODO: Implement

#     return wrapper

# Complete the code so it works as expected


def vowel_filter(function):
    def wrapper():
        all_letters = function()
        vowels = "aeiuoy"
        res = [l for l in all_letters if l in vowels]
        return res
    return wrapper
@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())

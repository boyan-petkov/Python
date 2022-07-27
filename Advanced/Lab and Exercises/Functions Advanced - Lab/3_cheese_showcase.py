# White a function called sorting_cheeses that receives keywords arguments:
# •	The key represents the name of the cheese
# •	The value is a list of quantities (integers) of the pieces of the given cheese
# The function should return the cheeses and their pieces' quantities sorted by the number of pieces of a cheese kind in descending order. 
# If two or more cheeses have the same number of pieces, sort them by their names in ascending order (alphabetically). 
# For each kind of cheese, return their pieces quantities in descending order.
# For more clarifications, see the examples below.

def sorting_cheeses(**kwargs):
    result = ""
    sorted_cheese = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    for tuple_ in sorted_cheese:
        final = sorted(tuple_[1], reverse= True )
        # return (tuple_[0]), "\n".join([str(el) for el in final])
        result += tuple_[0] + "\n" + "\n".join([str(el) for el in final]) + "\n"
        # result = result.strip()
    return result

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

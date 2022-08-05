# Spring is the season of new beginnings. Fresh buds bloom, animals awaken and the earth seems to come to life again.
# Farmers and gardeners plant their seeds and temperatures slowly rise.
# Write a function called start_spring which will receive a different number of keyword arguments.
# Each keyword holds a key with a name of the spring object (string), and each value holds its type (string). 
# For example, dahlia="flower", shrikes="bird", dogwood="tree".
# The function should sort the given spring objects in collections by their type:
# •	The collections sorted by their number of elements in descending order. 
# If two or more collections have the same number of elements in them, return them in ascending order (alphabetically) by the type's name. 
# •	Each collection's elements should be sorted in ascending order (alphabetically) by the object's name.
# Note: Submit only the function in the judge system
  
# Input
# •	There will be no input. Just parameters passed to your function.

# Output
# •	Return the result, sorted as described above in the format:
# o	"{type_one}:
# -{spring_object_of_this_type_one}
# -{spring_object_of_this_type_two}
# …
# -{spring_object_of_this_type_N}
# {type_two}:
# …
# {type_N}:
# …
# -{last_spring_object_of_typeN}"

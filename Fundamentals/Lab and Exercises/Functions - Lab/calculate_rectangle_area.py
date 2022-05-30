# Create a function that calculates and returns the area of a rectangle by given width and height. Print the result on the console.


def area_rectangle(w, h):
    area = w * h
    return area


width, height = int(input()), int(input())
print(area_rectangle(width, height))

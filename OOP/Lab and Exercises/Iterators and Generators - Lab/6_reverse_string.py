
# Create a generator function called reverse_text that receives a string and yield all string characters in reversed order.

def reverse_text(text):
    start = len(text) - 1
    end = 0
    while start >= end:
        yield text[start]
        start -= 1


for char in reverse_text("step"):
    print(char, end="")

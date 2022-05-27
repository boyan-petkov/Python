# As a good friend, you decide to buy presents for your friends.
# Create a program that helps you plan the gifts for your friends and family. First, you are going to receive the gifts you plan on buying on a single line, 
# separated by space, in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"
# Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
# •	"OutOfStock {gift}"
# o	Find the gifts with this name in your collection, if any, and change their values to "None".  
# •	"Required {gift} {index}"
# o	If the index is valid, replace the gift on the given index with the given gift. 
# •	"JustInCase {gift}"
# o	Replace the value of your last gift with this one. 
# In the end, print the gifts on a single line, except the ones with value "None", separated by a single space in the following format:
# "{gift1} {gift2} {gift3} … {giftn}"


gifts = input().split()
command = input()

while not command == "No Money":
    command = command.split()
    if "OutOfStock" in command:
        for i in range(len(gifts)):
            if command[1] in gifts[i]:
                gifts[i] = "None"
    elif "Required" in command:
        for i in range(len(gifts)):
            if i == int(command[2]):
                gifts[i] = command[1]
    elif "JustInCase" in command:
        gifts[-1] = command[1]
    command = input()
while "None" in gifts:
    gifts.remove("None")
for i in gifts:
    print(i, end=" ")

# You will be given a number. Print the largest number that can be formed from the digits of the given number.


number =input()
max_num = []

for el in number:
    max_num.append(el)
    sor = sorted(max_num, reverse= True)
print("".join(sor))

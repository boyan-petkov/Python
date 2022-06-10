# You are fed up with changing the version of your software manually. Instead, you will create a little script that will make it for you.
# You will be given a string representing the version of your software in the format: "{n1}.{n2}.{n3}". Your task is to print the next version. 
#   For example, if the current version is "1.3.4", the next version will be "1.3.5". 
# The only rule is that the numbers cannot be greater than 9. If it happens, set the current number to 0 and increase the previous number. 


current_version = list(map(int, input().split(".")))

if current_version[2] < 9:
    current_version[2] += 1
else:
    current_version[2] = 0
    if current_version[1] < 9:
        current_version[1] += 1
    else:
        current_version[1] = 0
        current_version[0] += 1
current_version = list(map(str, current_version))
print(".".join(current_version))

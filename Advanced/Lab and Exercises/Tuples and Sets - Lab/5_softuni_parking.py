# There is a party at SoftUni. Many guests are invited, and there are two types of them: Regular and VIP. 
#   When a guest comes, check if they exist on any of the two reservation lists.
# On the first line, you will receive the number of guests – N. On the following N lines, you will be receiving their reservation codes. 
# All reservation codes are 8 characters long, and all VIP numbers will start with a digit. Keep in mind that all reservation numbers must be unique.
# After that, you will be receiving guests who came to the party until you read the "END" command.
# In the end, print the number of guests who did not come to the party and their reservation numbers:
# •	The VIP guests must be first.
# •	Both the VIP and the Regular guests must be sorted in ascending order

def vip_or_not(current_code):
    if current_code[0].isdigit():
        vips.add(current_code)
    elif current_code[0].isalpha():
        regular.add(current_code)
    return vips, regular


def if_they_come(current_code):
    if current_code in vips:
        vips.remove(current_code)
    if current_code in regular:
        regular.remove(current_code)
    return vips, regular


#
def union_and_print(sets1, sets2):
    final = sets1.union(sets2)
    # final = list(final)
    # final.sort()
    print(len(final))
    print("\n".join(sorted(final)))


invites_number = int(input())

vips = set()
regular = set()

for _ in range(invites_number):
    vip_or_not(input())

cmd = input()
while not cmd == "END":
    if_they_come(cmd)
    cmd = input()

union_and_print(vips, regular)



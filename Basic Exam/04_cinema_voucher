sum_voucher = int(input())

number_of_tickets = 0
number_of_other_purchase = 0
command = input()
price = 0

while command != "End":
    length = len(command)
    if length > 8:
        price = ord(command[0]) + ord(command[1])
        if price > sum_voucher:
            break
        else:
            sum_voucher -= price
            number_of_tickets += 1
    else:
        price = ord(command[0])
        if price > sum_voucher:
            break
        number_of_other_purchase += 1
        sum_voucher -= ord(command[0])
    command = input()
    
print(number_of_tickets)
print(number_of_other_purchase)

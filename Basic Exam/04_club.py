predicted_income = float(input())

income = 0
order_price = 0

command = input()
while command != "Party!" and income <= predicted_income:
    cocktails_number = int(input())
    order_price = (len(command) * cocktails_number)
    if order_price % 2 == 0:
        income += order_price
    else:
        order_price *= 0.75
        income += order_price
    if command == "Party!" or income >= predicted_income:
        break
    command = input()

diff = abs(predicted_income - income)

if command == "Party!":
    print(f"We need {diff:.2f} leva more.")
    print(f"Club income - {income:.2f} leva.")
if income >= predicted_income:
    print("Target acquired.")
    print(f"Club income - {income:.2f} leva.")
    

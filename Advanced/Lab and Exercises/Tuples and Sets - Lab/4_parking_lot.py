# Write a program that:
# •	Records a car number for every car that enters the parking lot
# •	Removes a car number when the car leaves the parking lot
# On the first line, you will receive the number of commands - N. 
# On the following N lines, you will receive the direction and car's number in the format: "{direction}, {car_number}". 
# The direction could only be "IN" or "OUT". Print the car numbers which are still in the parking lot. 
# Keep in mind that all car numbers must be unique. If the parking lot is empty, print "Parking Lot is Empty".
# Note: The order in which we print the result does not matter.

def parking_lot(current_car):
    direction, number = current_car.split(", ")
    if direction == "IN":
        lot.add(number)
    elif direction == "OUT":
        lot.remove(number)
    return lot


def print_them(some_collection):
    if not some_collection:
        print("Parking Lot is Empty")
    else:
        print("\n".join(some_collection))


number_of_commands = int(input())

lot = set()

for _ in range(number_of_commands):
    parking_lot(input())

print_them(lot)

# You are driving a truck on a circle road with N petrol pumps on it. The petrol pumps are numbered 0 to (N−1) (both inclusive).
# For each petrol pump you will receive two pieces of information (separated by a single space): 
# -	the amount of petrol that petrol pump will give
# -	the distance from that petrol pump to the next petrol pump (kilometers)
# Initially, you have a tank of infinite capacity carrying no petrol. 
# The truck can start the tour at any of the petrol pumps and it will move one kilometer for each liter of the petrol.
# Calculate the first point from where the truck will be able to complete the circle. Consider that the truck will stop at each of the petrol pumps. 

# Input
# •	On the first line you will receive the number of petrol pumps - N
# •	On the next N-lines you will receive the amount of petrol that petrol pump will give and 
# the distance between that petrol pump and the next petrol pump, separated by single space

# Output
# •	An integer which will be the smallest index of a petrol pump from which you can start the tour

# Constraints
# •	1 ≤ N ≤ 1000001
# •	1 ≤ Amount of petrol, Distance ≤ 1000000000
# •	You will always have at least one point from where the truck will be able to complete the circle

from collections import deque

pumps = deque()

n_pumps = int(input())
for _ in range(n_pumps):
    liters, km = input().split()
    pumps.append([int(liters), int(km)])


for i in range(n_pumps):
    fuel_tank = 0
    pumps_travelled = 0
    for gas_pump in pumps:
        liters, km = gas_pump[0], gas_pump[1]
        fuel_tank += liters
        if fuel_tank >= km:
            pumps_travelled += 1
            fuel_tank -= km
        else:
            fuel_tank = 0
            pumps_travelled = 0
            break
    if pumps_travelled == n_pumps:
        print(i)
        break
    pumps.rotate(-1)



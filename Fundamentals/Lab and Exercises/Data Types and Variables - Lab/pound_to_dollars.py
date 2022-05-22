# Write a program that converts British pounds (integer) to US dollars formatted to the 3rd decimal point.
# 1 British Pound = 1.31 Dollars.


pound = float(input())

dollars = pound * 1.31

print(f"{dollars:.3f}")

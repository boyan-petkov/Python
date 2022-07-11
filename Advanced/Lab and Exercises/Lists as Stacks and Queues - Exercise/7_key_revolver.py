# Our favorite super-spy action hero Sam is back from his vacation and it is time to go on a mission.
# He needs to unlock a safe locked by several locks in a row, which all have varying sizes.
# The hero posesses a special weapon though, called the Key Revolver, with special bullets.
# Each bullet can unlock a lock with a size equal to or larger than the size of the bullet. 
# The bullet goes into the keyhole, then explodes, completely destroying it. 
# Sam doesn't know the size of the locks, so he needs to just shoot at all of them, until the safe runs out of locks.
# What's behind the safe, you ask? Well, intelligence! It is told that Sam's sworn enemy – Nikoladze, 
# keeps his top secret Georgian Chacha Brandy recipe inside. 
# It's valued differently across different times of the year, so Sam's boss will tell him what it's worth over the radio.
# One last thing, every bullet Sam fires will also cost him money, which will be deducted from his pay from the price of the intelligence. 
# Good luck, operative.

# Input
# •	On the first line of input, you will receive the price of each bullet – an integer in the range [0-100]
# •	On the second line, you will receive the size of the gun barrel – an integer in the range [1-5000]
# •	On the third line, you will receive the bullets – a space-separated integer sequence with [1-100] integers
# •	On the fourth line, you will receive the locks – a space-separated integer sequence with [1-100] integers
# •	On the fifth line, you will receive the value of the intelligence – an integer in the range [1-100000]
# After Sam receives all of his information and gear (input), he starts to shoot the locks front-to-back, while going through the bullets back-to-front.
# If he successfully destroyed a lock, print "Bang!", then remove the lock. If not, print "Ping!", leaving the lock intact. 
# The bullet is removed in both cases.
# If Sam runs out of bullets in his barrel, print "Reloading!" on the console, then continue shooting. If there aren't any bullets left, don't print it.
# The program ends when Sam either runs out of bullets, or the safe runs out of locks.

# Output
# •	If Sam manages to open the safe, print:
# "{bullets_left} bullets left. Earned ${money_earned}" 
# •	Otherwise, print:
# "Couldn't get through. Locks left: {locks_left}"
# Make sure to account the price of the bullets when calculating the money earned.

# Constraints
# •	The input will be within the constaints specified above and will always be valid. There is no need to check it explicitly.
# •	There will never be a case where Sam breaks the lock and ends up with а negative balance.


from collections import deque

price_per_bullet = int(input())
gun_barrel = int(input())
bullets = deque(int(x) for x in (input()).split())  # LIFO
locks = deque(int(x) for x in input().split())  # FIFO
money = int(input())
start_bullets = bullets.copy()

shoots = 0
while bullets and locks:
    if shoots == gun_barrel and bullets:
        print("Reloading")
        shoots = 0
    bullet, lock = bullets.pop(), locks.popleft()
    if bullet <= lock:
        print("Bang!")
        shoots += 1
    else:
        print("Ping!")
        locks.appendleft(lock)
        shoots += 1
    if shoots == gun_barrel and bullets:
        print("Reloading!")
        shoots = 0

money_left = money - (len(start_bullets) - len(bullets)) * price_per_bullet
if not locks:
    print(f"{len(bullets)} bullets left. Earned ${money_left}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")


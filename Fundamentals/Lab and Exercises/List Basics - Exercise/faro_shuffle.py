# A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half. 
# Then the cards in the two halves are perfectly interleaved, such that the original bottom card is still on the bottom and the original top card is still on top.
# For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six'] once, gives ['ace', 'four', 'two', 'five', 'three', 'six']
# Write a program that receives a single string (cards separated by space) and on the second line receives a count of faro shuffles that should be made. 
# Print the state of the deck after the shuffle.
# Note: The length of the deck of cards will always be an even number.


cards = input().split()
shuffles = int(input())

final_cards = []

for shuffles in range(shuffles):
    left_side = cards[:len(cards) // 2]
    right_side = cards[len(cards) // 2:]
    final_cards = []
    for index in range(len(left_side)):
        final_cards.append(left_side[index])
        final_cards.append(right_side[index])
        cards = final_cards
print(final_cards)


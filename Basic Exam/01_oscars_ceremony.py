rent_for_room = int(input())

statuete = rent_for_room * 0.70
catering = statuete * 0.85
audio_effects = catering * (1 / 2)

total_costs = rent_for_room + statuete + catering + audio_effects

print(f"{total_costs:.2f}")

# Here comes the final and the most interesting part – the Final ranking of the candidate-interns. 
# The final ranking is determined by the points of the interview tasks and by the points from the exams in SoftUni. Here is your final task. 
# You will receive some lines of input in the format "{contest}:{password for contest}" until you receive "end of contests". 
# Save that data because you will need it later. 
# After that you will receive other type of inputs in format "{contest}=>{password}=>{username}=>{points}" until you receive "end of submissions". 
# Here is what you need to do.
# •	Check if the contest is valid (It is considered valid if you received it in the first type of input)
# •	Check if the password is correct for the given contest
# •	If the contest and the password is valid, save the user with the contest they take part in (a user can take part in many contests) and 
# the points the user has in the given contest. If you receive the same contest and the same user update the points only if the new ones are more than the older ones.
# In the end, you should print the info for the user with the most points (total points for all contents they participated in) in the format "Best candidate is {user} with total {total_points} points.". After that print all students ordered by their names. For each user print each contest with the points in descending order. See the examples.

# Output
# •	On the first line, print the best user in format "Best candidate is {user} with total {total points} points.".
# •	Then print all students ordered as mentioned above in format:
# "{user_name1}
# #  {contest1} -> {points}
# #  {contest2} -> {points} 
# …
# #  {contestN} -> {points}"


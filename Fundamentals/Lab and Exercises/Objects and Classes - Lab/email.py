# Create class Email. The __init__ method should receive sender, receiver and a content. It should also have a default set to False attribute called is_sent. 
# The class should have two additional methods:
# •	send() - sets the is_sent attribute to True
# •	get_info() - returns the following string: "{sender} says to {receiver}: {content}. Sent: {is_sent}"
# You will receive some information (separated by a single space) until you receive the command "Stop". 
# The first element will be the sender, the second one – the receiver, and the third one – the content.
# On the final line, you will be given the indices of the sent emails separated by comma and space ", ". 
# Call the send() method for the given indices of emails. For each email, call the get_info() method.


# Input
# Peter John Hi,John
# John Peter Hi,Peter!
# Katy Lilly Hello,Lilly
# Stop
# 0, 2

# Output
# Peter says to John: Hi,John. Sent: True
# John says to Peter: Hi,Peter!. Sent: False
# Katy says to Lilly: Hello,Lilly. Sent: True

# Example 2
# Input
# Peter John Hi,John
# John Peter Hi,Peter!
# Katy Lilly Hello,Lilly
# Stop

# Output
# 0, 2	Peter says to John: Hi,John. Sent: True
# John says to Peter: Hi,Peter!. Sent: False
# Katy says to Lilly: Hello,Lilly. Sent: True


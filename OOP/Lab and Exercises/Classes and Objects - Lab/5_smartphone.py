# Create a class called Smartphone. Upon initialization it should receive a memory (number). 
# It should also have 2 other instance attributes: apps (empty list by default) and is_on (False by default). Create 3 methods:
# -	power() - sets is_on on True if the phone is off, otherwise sets it to False
# -	install(app, app_memory)
# o	If there is enough memory on the phone and it is on, install the app (add it to apps and decrease the memory of the phone) and return "Installing {app}"
# o	If there is enough memory, but the phone is off, return "Turn on your phone to install {app}"
# o	Otherwise return "Not enough memory to install {app}"
# -	status() - returns "Total apps: {total_apps_count}. Memory left: {memory_left}"


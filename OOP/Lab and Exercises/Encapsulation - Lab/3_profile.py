Create a class called Profile. Upon initialization it should receive:
•	username: str - the username should be between 5 and 15 characters (inclusive). 
  If it is not, raise a ValueError with message "The username must be between 5 and 15 characters."
•	password: str - the password must be at least 8 characters long; it must contain at least one upper case letter and at least one digit. 
  If it does not, raise a ValueError with message "The password must be 8 or more characters with at least 1 digit and 1 uppercase letter."
Hint: Use Getters and Setters to name mangle them. 
Override the __str__() method of the base class so it returns: "You have a profile with username: "{username}" and password: 
  {"*" with the length of password}".


# Create a class called Time. Upon initialization, it should receive hours, minutes, and seconds (integers).
# The class should also have class attributes max_hours equal to 23, max_minutes equal to 59, and max_seconds equal to 59. 
# You should also create 3 additional instance methods:
# -	set_time(hours, minutes, seconds) - updates the time with the new values
# -	get_time() - returns "{hh}:{mm}:{ss}"
# -	next_second() - updates the time with one second (use the class attributes for validation) and returns the new time (use the get_time() method)

class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        self.seconds += 1
        if self.seconds > Time.max_seconds:
            self.minutes += 1
            self.seconds = 0
            if self.minutes > Time.max_minutes:
                self.hours += 1
                self.minutes = 0
                if self.hours > Time.max_hours:
                    self.hours = 0
        return self.get_time()



time = Time(9, 30, 52)
print(time.next_second())

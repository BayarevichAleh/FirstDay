class MyTime:
    def __init__(self, hours=None, minutes=None, seconds=None):
        if type(hours) == int and type(minutes == int) and type(seconds == int):
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds
        elif type(hours) == type(self) and minutes == None and seconds == None:
            self.hours = hours.hours
            self.minutes = hours.minutes
            self.seconds = hours.seconds
        elif type(hours) == str and minutes == None and seconds == None:
            a = hours.split()
            if type(a) == list and len(a) == 3 and a[0].isdigit() and a[1].isdigit() and a[2].isdigit():
                self.hours = int(a[0])
                self.minutes = int(a[1])
                self.seconds = int(a[2])
            else:
                self.hours = 0
                self.minutes = 0
                self.seconds = 0

    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds

    def __ne__(self, other):
        return self.hours != other.hours or self.minutes != other.minutes or self.seconds != other.seconds

    def __le__(self, other):
        a = self.hours * 3600 + self.minutes * 60 + self.seconds
        b = other.hours * 3600 + other.minutes * 60 + other.seconds
        return a <= b

    def __lt__(self, other):
        a = self.hours * 3600 + self.minutes * 60 + self.seconds
        b = other.hours * 3600 + other.minutes * 60 + other.seconds
        return a < b

    def __ge__(self, other):
        a = self.hours * 3600 + self.minutes * 60 + self.seconds
        b = other.hours * 3600 + other.minutes * 60 + other.seconds
        return a >= b

    def __gt__(self, other):
        a = self.hours * 3600 + self.minutes * 60 + self.seconds
        b = other.hours * 3600 + other.minutes * 60 + other.seconds
        return a > b

    def __add__(self, other):
        self.hours += other.hours
        self.minutes += other.minutes
        self.seconds += other.seconds
        if self.seconds > 56:
            self.minutes += int(self.seconds / 60)
            self.seconds = self.seconds % 60
        if self.minutes > 59:
            self.hours += int(self.minutes / 60)
            self.minutes = self.minutes % 60

    def __sub__(self, other):
        self.hours -= other.hours
        self.minutes -= other.minutes
        self.seconds -= other.seconds

    def __mul__(self, number):
        a = self.hours * 3600 + self.minutes * 60 + self.seconds
        a *= number
        self.hours = int(a / 3600)
        self.minutes = int(a % 3600 / 60)
        self.seconds = a % 60

    def __str__(self):
        str_hours = f"{self.hours}"
        str_minutes = f"{self.minutes}"
        str_seconds = f"{self.seconds}"

        if self.hours < 10:
            str_hours = f"0{self.hours}"
        if self.minutes < 10:
            str_minutes = f"0{self.minutes}"
        if self.seconds < 10:
            str_seconds = f"0{self.seconds}"

        return f"{str_hours}:{str_minutes}:{str_seconds}"


a = MyTime("5 30 30")
b = MyTime(12, 45, 19)

print(a <= b)
print(a >= b)
print(a < b)
print(a > b)
a + b
print(a)

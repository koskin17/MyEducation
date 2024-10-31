class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @property
    def date(self):
        if len(str(self.day)) < 2:
            self.day = str(self.day).zfill(2)
        if len(str(self.month)) < 2:
            self.month = str(self.month).zfill(2)
        if len(str(self.year)) < 4:
            self.year = str(self.year).zfill(4)

        return f"{self.day} / {self.month} / {self.year}"

    @property
    def usa_date(self):
        return f"{self.month}-{self.day}-{self.year}"


d1 = Date(5, 10, 2001)
d2 = Date(15, 3, 999)

print(d1.date)
print(d1.usa_date)
print(d2.date)
print(d2.usa_date)

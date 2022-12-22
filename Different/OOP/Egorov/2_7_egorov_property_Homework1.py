class Money:
    def __init__(self, dollars, cent):
        self.total_cents = dollars * 100 + cent

    @property
    def dollars(self):
        return self.total_cents // 100  # делим нацело на 100

    @dollars.setter
    def dollars(self, new_dollars):
        if isinstance(new_dollars, int) and new_dollars >= 0:
            self.total_cents = new_dollars * 100 + self.cents
        else:
            print("Error dollars")

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, new_cents):
        if isinstance(new_cents, int) and 0 < new_cents < 100:
            self.total_cents = self.total_cents - self.cents + new_cents
        else:
            print("Error cent")

    def __str__(self):
        return f"Ваше состояние составляет {self.dollars} долларов {self.cents % 100} центов"

    # Данные строки кода переведены в свойство property для методово getter и setter
    # dollars = property(fget=get_dollars, fset=set_dollars)
    # cent = property(fget=get_cents, fset=set_cents)


Bill = Money(101, 99)
print(Bill)
print(Bill.dollars, Bill.cents)
print(Bill.total_cents)
Bill.dollars = 666
print(Bill)
Bill.cents = 12
print(Bill)

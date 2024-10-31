class PizzaMaker:
    def __make_pepperoni(self):
        print("Pepperoni")

    def __make_barbecue(self):
        print("Barbecue")

maker = PizzaMaker()
print(PizzaMaker.__dict__.keys())
print(maker._PizzaMaker__make_pepperoni)
print(maker._PizzaMaker__make_barbecue)

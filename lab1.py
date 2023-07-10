class Bike:
    colour = ""
    model = ""
    brand = ""
    no_of_units = 7
    base_price = 100

    def __init__(self, brand, model, colour) -> None:
        self.colour = colour
        self.model = model
        self.brand = brand

    def __str__(self) -> str:
        return "I am gonna buy a bike"

    def price(self):
        return self.no_of_units * self.base_price


bike = Bike("RE", "Bullet", "SandStorm")
print(bike)
print(bike.colour)
print(bike.price())

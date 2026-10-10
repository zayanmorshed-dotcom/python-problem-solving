class Smartphone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

class GamingPhone(Smartphone):
    def __init__(self, brand, price, cooling_system):
        super().__init__(brand, price)
        self.cooling_system = cooling_system

phone1 = GamingPhone("ASUS ROG", 150000, "Liquid Cooling")

print("Brand:", phone1.brand)
print("Price:", phone1.price)
print("Cooling System:", phone1.cooling_system)

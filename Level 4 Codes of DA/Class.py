class Car:
    brand = ""
    price = 0


my_car = Car()
my_car.brand = "Toyota"
my_car.price = 2500000

print("Brand:", my_car.brand)
print("Price:", my_car.price)



class Smartphone:
    def setDetails(self, brand, price):
        self.brand = brand
        self.price = price

    def showDetails(self):
        print(f"Smartphone Details - Brand: {self.brand}, Price: {self.price} BDT")

phone1 = Smartphone()
phone1.setDetails("Samsung", 85000)

phone2 = Smartphone()
phone2.setDetails("Apple", 120000)

phone1.showDetails()
phone2.showDetails()

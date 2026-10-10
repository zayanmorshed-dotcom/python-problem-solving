class Car:
    name = ""
    colour = ""
    model = ""

my_first_car = Car()
my_first_car.name = "BMW"       
my_first_car.colour = "Red"
my_first_car.model = "M5"

print(f"My car brand: {my_first_car.name},  My car colour: {my_first_car.colour},My car Model: {my_first_car.model}")










class Car:
    name = ""
    color = ""
    def setValue(self, n, c):
        self.name = n
        self.color = c
    def printCar(self):
        print(f"My car brand: {self.name}, My car color: {self.color}")

my_first_car = Car()
my_first_car.setValue("BMW", "BLACK")
my_first_car.printCar()

second_car = Car()
second_car.setValue("BYD", "GRAY")
second_car.printCar()

# print(f"My car brand: {second_car.name}, My car color: {second_car.color}")

# my_first_car.name = "Toyota"
# my_first_car.color = "Black"
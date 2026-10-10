class Animal:
    def make_sound(self):
        print("The animal makes a sound.")


class Dog(Animal):
    def make_sound(self):
        print("The dog barks: WOOF WOOF!")

class Cat(Animal):
    def make_sound(self):
        print("The cat meows: MEOW MEOW!")

my_dog = Dog()
my_dog.make_sound()  # Output: The dog barks: WOOF WOOF!

my_cat = Cat()
my_cat.make_sound()  # Output: The cat meows: MEOW MEOW!



class Calculator:
    def add(self, a, b, c = None):
        if c is not None:
            print(f"Sum of three numbers: {a + b + c}")
        else:
            print(f"Sum of two numbers: {a + b}")





my_cal = Calculator()
my_cal.add(10, 20)
my_cal.add(10, 20, 50)
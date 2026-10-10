class Greeter:
    def say_hello(self, name1, name2=None):
        if name2 is not None:
            print(f"Hello {name1} and {name2}!")
        else:
            print(f"Hello {name1}!")

g = Greeter()
g.say_hello("Zayan")
g.say_hello("Zayan", "Ronaldo")

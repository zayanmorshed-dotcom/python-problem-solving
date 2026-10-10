class Dog:
    def return_sound(self):
        return "Woof!"

class Cat:
    def return_sound(self):
        return "Meow!"

def animal_party(animal_object):
    print(animal_object.return_sound())
    
dog1 = Dog()    
cat1 = Cat()
animal_party(dog1)
animal_party(cat1)

class Light:
    def turn_on(self):
        print("The light is on.")

class Fan:
    def turn_on(self):
        print("The fan is on.")

class AirConditioner:
    def turn_on(self):
        print("The air conditioner is on.")

def active_device(device_object):
    device_object.turn_on()

my_light = Light()
my_fan = Fan()  
my_ac = AirConditioner()

print(".....Activating devices:")
active_device(my_light)
active_device(my_fan)
active_device(my_ac)
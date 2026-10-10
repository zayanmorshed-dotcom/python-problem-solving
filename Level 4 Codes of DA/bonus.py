class Manager:
    def bonus(self):
        return "Manager bonus is 50000"

class Developer:
    def bonus(self):
        return "Developer bonus is 30000"

def show_bonus(employee_object):
    print(employee_object.bonus())

m = Manager()
d = Developer()

show_bonus(m)
show_bonus(d)

class StudentProfile:
    def __init__(self, name, id, cgpa):
        self.name = name        # public
        self._id = id           # protected
        self.__cgpa = cgpa      # private

    def show_cgpa(self):
        print(f"CGPA: {self.__cgpa}")

student1 = StudentProfile("Zayan", 101, 3.85)

print(student1.name)       # public
print(student1._id)        # protected
student1.show_cgpa()       # private via method

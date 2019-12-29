class Person:
    def __init__(self, arg_fname, arg_lname, arg_age):
        self.firstname = arg_fname
        self.lastname = arg_lname
        self.age = arg_age

    def compute_fullname(self):
        self.fullname = self.firstname + " " + self.lastname

gagan = Person("Gagan", "Multani", 27)
sandeep = Person("Sandeep", "Multani", 29)

print(gagan.firstname)
print(sandeep.age)
gagan.compute_fullname()
print(gagan.fullname)
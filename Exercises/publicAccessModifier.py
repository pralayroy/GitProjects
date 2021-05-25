class Person:
    # Constructor
    def __init__(self, name, age):
        # Public data members
        self.person_name = name
        self.person_age = age
    # public member fuction
    def displayAge(self):
        print("Age: ", self.person_age)


obj = Person("Pralay", 34)
print("Name: ", obj.person_name)
obj.displayAge()

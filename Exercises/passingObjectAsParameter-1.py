from passingObjectAsParameter import MyClass


class Person:
    def __init__(self, name, age):
        print("init called")
        self.name = name
        self.age = age

    def display(self):
        print("in display")
        print("Name- ", self.name)
        print("Age- ", self.age)
        # object of MyClass
        obj = MyClass()
        obj.myMethod(self)    # Passing person object to method of MyClass (self = person here)


person = Person("Pralay", 34)
person.display()

class Student:
    # Class Variable
    stream = "ECE"

    def __init__(self, roll, address):
        # Instance Variable
        self.address = address
        self.roll = roll

    def getStudentAddress(self):
        print("Address is :", self.address)

    def getStudentRoll(self):
        print("Roll no is: ", self.roll)


s = Student("Bengaluru", 123)
s.getStudentAddress()
s.getStudentRoll()
print(s.stream)

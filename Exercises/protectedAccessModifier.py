# Super class
class Student:
    # Protected data members
    _studentName = None
    _studentRoll = None
    _studentBranch = None

    # Constructor
    def __init__(self, name, roll, branch):
        self._studentName = name
        self._studentRoll = roll
        self._studentBranch = branch

    # Protected member function
    def _displayRollAndBranch(self):
        print("Roll No: ", self._studentRoll)
        print("Branch Name: ", self._studentBranch)


# Derived class
class Person(Student):

    # Constructor
    def __init__(self, name, roll, branch):
        Student.__init__(self, name, roll, branch)

    # Public member function
    def displayDetails(self):

        # Accessing protected data member of super class
        print("Student Name: ", self._studentName)
        # Accessing protected member function of super class
        self._displayRollAndBranch()


obj = Person("Pralay", 14534, "ECE")
obj.displayDetails()



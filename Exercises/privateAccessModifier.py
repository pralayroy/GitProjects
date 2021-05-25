class Student:
    # private members
    __studentName = None
    __studentRollNo = None
    __studentBranch = None

    def __init__(self, name, roll, branch):

        self.__studentName = name
        self.__studentRollNo = roll
        self.__studentBranch = branch

    # private member function
    def __displayDetails(self):
        # accessing private data members
        print("Name is: ", self.__studentName)
        print("Roll No: ", self.__studentRollNo)
        print("Branch: ", self.__studentBranch)

    # public member function
    def accessPrivateFunction(self):
        # accesing private member function
        self.__displayDetails()


obj = Student("Pralay", 13423, "ECE")
obj.accessPrivateFunction()



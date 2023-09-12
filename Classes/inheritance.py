class Student:

# To define attributes of a class use init method
    def __init__(self, name, rollnumber):
# Self is used to initilize parameters
        self.name = name
        self.rollnumber = rollnumber


# Define Various Methods/Functions of class

    def getdata(self):
        print("Accepting Data")
        self.name = input('Enter Name:')
        self.rollnumber = input('Enter Rollnumber:')

    def putdata(self):
        print('The Name is:'+self.name)
        print('Roll Number is:'+self.rollnumber)

# Create another class MCA STUDENTS

class MCA_Student(Student):

    def __init__(self,age):
        self.age = age

    def MCA(self):
        print("I'm a student of MCA. My age is" +str(self.age))
        
# Create an object Kulbir
Kulbir = MCA_Student(27)
Kulbir.MCA()

# Let Object Kulbir use methods define in Student Class

Kulbir.getdata()
Kulbir.putdata()




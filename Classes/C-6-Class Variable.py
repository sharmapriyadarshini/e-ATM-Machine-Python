'''Instance variables are for data unique to each instance and class variables
are for attributes and methods shared by all instances of the class.
'''

class Employee():
    
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary      

    def increment(self):
        self.salary = int(self.salary * 1.08)


emp_1 = Employee("Saurabh", "Kaushal", 10000)
emp_2 = Employee("Vishal", "Mahajan", 20000)


print('Previous Salary: ' + str(emp_1.salary))

emp_1.increment()

print('Incremented Salary: ' + str(emp_1.salary))



'''Class Variables can be called using Class Itself or by an Instance of a Class
'''

class Employee:

    Percent_To_Be_Incremented = 1.04
    
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary      

  #  def increment(self):
   #     self.salary = int(self.salary * Percent_To_Be_Incremented)

 #   def increment(self):
 #       self.salary = int(self.salary * Employee.Percent_To_Be_Incremented)

    def increment(self):
        self.salary = int(self.salary * self.Percent_To_Be_Incremented)



emp_1 = Employee("Saurabh", "Kaushal", 10000)
emp_2 = Employee("Vishal", "Mahajan", 20000)



print('Previous Salary: ' + str(emp_1.salary))

#emp_1.increment()
##OR 
Employee.increment(emp_1)

print('Incremented Salary: ' + str(emp_1.salary))

'''We can acces the class variable from class itself as well as from its instance
i.e. emp_1 & emp_2. Uncommment the below to Understand'''

print(Employee.Percent_To_Be_Incremented)
print(emp_1.Percent_To_Be_Incremented)
print(emp_2.Percent_To_Be_Incremented)


''' When we try to access attribute from an instance it will first check if instance contains
that attribute and if it doesn't then it see if class or any class it inherits from contains
that attribute.
 '''




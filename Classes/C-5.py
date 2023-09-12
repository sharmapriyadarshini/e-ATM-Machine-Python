class Employee():
    
        def __init__(self, fname, lname, salary):
           self.fname = fname
           self.lname = lname
           self.salary = salary
           self.email = fname + '.' + lname + "@relearn.org.in"

        def fullname(self):
            return '{}{}'.format(self.fname, self.lname)
    
''' Each Method within a class automatically takes the instance as the first
argument'''

emp_1 = Employee('Saurabh', 'Kaushal', 10000)
emp_2 = Employee('Vishal', 'Mahajan', 20000)

print(emp_2.fullname())

# OR

#print(Employee.fullname(emp_2))

#print(emp_1.fullname())

#print(Employee.fullname(emp_1))






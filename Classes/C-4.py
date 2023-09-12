class Employee:
    
    ''' Problem with C-2 is that we need to assign the attributes of
every employee separately. To automate this we will use init method.
When a class defines an __init__() method, class instantiation automatically
invokes __init__() for the newly-created class instance.
The __init__() method may have arguments for greater flexibility. In that case,
arguments given to the class instantiation operator are passed on to __init__()'''



    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.email = fname + '.' + lname + "@relearn.org.in"

emp_1 = Employee('Saurabh', 'Kaushal', 10000)
emp_2 = Employee('Vishal', 'Mahajan', 20000)

''' TO PRINT THE FULL NAME WE ARE USING TWO PLACE HOLDERS {}{} BUT TO WRITE FULL NAME 
 EVERYTIME OF EVERY EMPLOYEE IT WILL BE A LONG METHOD SO WE WILL CREATE A NEW
 METHOD INSIDE THE CLASS EMPLOYEE'''

print ('{}{}'.format(emp_1.fname, emp_1.lname))







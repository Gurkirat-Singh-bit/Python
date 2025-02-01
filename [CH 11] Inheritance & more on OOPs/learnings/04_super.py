# here i learnt how to use the super method
 

class empolyee():


    def __init__(self):
         
         print("object is being created")
    
    def details(self,name , age,mobile_no):

        self.name = name

        self.age =  age
        
        self.mobile_no = mobile_no

class manager(empolyee):

    
    def manage(self,expirence,no_employee):

        self.expirence = expirence

        self.no_employee = no_employee

class developer(manager):
    
    def work(self, project):
        
        self.project = project

    def fun(self):
         
        super().__init__()                                  # used for calling a method inside a child class from parent class it can also call constructor
    

    def display(self):
            print(f"Name: {self.name}, Age: {self.age}, Mobile No: {self.mobile_no}")

            print(f"Experience: {self.expirence}, No of Employees: {self.no_employee}")

            print(f"Project: {self.project}")

# Example usage

dev = developer()

dev.details("John Doe", 30, "1234567890")

dev.manage(5, 10)

dev.work("AI Project")

dev.display()

dev.fun()

# Output:
# Name: John Doe, Age: 30, Mobile No: 1234567890
# Experience: 5, No of Employees: 10
# object is being created



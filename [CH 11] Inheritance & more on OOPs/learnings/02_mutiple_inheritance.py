# here i learnt mutiple inheritance in python

class empolyee():

    def details(self,name , age,mobile_no):
        
        self.name = name
        
        self.age = age

        self.mobile_no = mobile_no
        

class manager():

    def manage(self,expirence,no_employee):

        self.expirence = expirence

        self.no_employee = no_employee

class developer(empolyee,manager):

    def work(self, project):
        
        self.project = project


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
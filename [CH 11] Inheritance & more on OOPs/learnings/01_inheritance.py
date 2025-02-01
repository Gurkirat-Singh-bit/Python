# here i learnt inheritance(single) in python

class programmer:                                         # this is parent class 

 
    company = "Google"                                    # class attribute 
              
    
    job = "programmer"                                    # class attribute 

    def show(self):                                       # method intialise


      print(f"this {self.job} is of {self.company}")      # printing 


class developer(programmer):                              # child class which share the property of parent class
   
   job = "developer"                                      # class attribute

   def job(self):                                         # method intialise 
      
      self.job = "developer"                              # by caliing this method its changes the job attribute

      self.show()                                         # this call function from the parent class 
    
   def showlanguage(self):                                # method intialise
        
        print(f"this developer knows {self.language}")


employee1 = programmer()

employee1.show()

employee2 = developer()

employee2.job()

employee2.language = "python"

employee2.showlanguage()
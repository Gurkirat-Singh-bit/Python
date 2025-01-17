# Problem 5) Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways.




from random import randint                                                                              # Importing the randint function from the random module to generate random numbers


class train:                                                                                            # Defining a class named 'train'

    
    def __init__(self, name, trainNO):                                                                  # Initializing the class with name and train number

        self.name = name                                                                                # Assigning the name of the train
        
        self.trainNo = trainNO                                                                          # Assigning the train number

   
    def tobook(self, fro, to, berth, tier):                                                             # Method to book a ticket

        print(f"YOUR TICKET has been successfully booked from {fro} to {to} in {berth} of {tier} tier") # Printing the booking details

    
    def getfare(self, fro, to, berth, tier):                                                            # Method to get fare information
       
        print(f"the fare from {fro} to {to} in {berth} of {tier} tier is {randint(250, 2500)}")         # Printing the fare details with a random fare amount

    
    def getstatus(self):                                                                                # Method to get the status of the train
        
        print(f"the train no {self.trainNo} is 1hr 24min late")                                         # Printing the status of the train

# Creating an instance of the train class with name and train number
train1 = train("Gurkirat singh", 25699)

# Booking a ticket using the tobook method
train1.tobook("jagadhri workshop", "Nilokheri", "side lower", "3ac")

# Getting fare information using the getfare method
train1.getfare("jagadhri workshop", "Nilokheri", "side lower", "3ac")

# Getting the status of the train using the getstatus method
train1.getstatus()
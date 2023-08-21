class Garage():
    tickets = []
    parkingSpaces = []
    currentTicket = {"paid": False,}
    for i in range(100):
        tickets.append("ticket")
        parkingSpaces.append("parking space")

    def takeTicket(self):
        self.tickets.pop()
        self.parkingSpaces.pop()
        numSpots = len(self.parkingSpaces)
        print(f"Number of spots left: {numSpots}\n")

    def payForParking(self):
        flag = True
        while flag:
            pay = input("Please enter 5 to pay $5 for parking.\n")
            try:
                if int(pay) == 5:
                    print("Your ticket has been paid you have 15mins to leave.\n")
                    self.currentTicket["paid"] = True
                    flag = False
                else:   
                    print("You haven't paid yet.\n")
            except:
                print("Please enter in a number.\n")

    def leaveGarage(self):
        if self.currentTicket["paid"]:
            print("Thank you, have a nice day\n")
            self.tickets.append("ticket")
            self.parkingSpaces.append("parking space")
            self.currentTicket["paid"] = False
        else:
            self.payForParking()
            print("Thank you, have a nice day\n")
            self.tickets.append("ticket")
            self.parkingSpaces.append("parking spot")
            self.currentTicket["paid"] = False
    
    def handler(self):
        flag = True
        while flag:
            print("Welcome to the parking garage.\n")
            print("Enter t to take a ticket.")
            print("Enter p to pay for parking.")
            print("Enter l to leave the parking garage.\n")
            choice = input("What would you like to do?")

            if choice == "t":
                self.takeTicket()
            elif choice == "p":
                self.payForParking()
            elif choice == "l":
                self.leaveGarage()
            else:
                print("Invalid Input.")

parkingGarage = Garage()
parkingGarage.handler()

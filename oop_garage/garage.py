class Garage():

    def __init__(self, tickets, spaces, price, stubs):
        self.tickets = tickets
        self.spaces = spaces
        self.price = price
        self.stubs = stubs

    def ticketCount(self):
        paid = 0
        for i in self.stubs.values():
            if i == "PAID":
                paid += 1
        print(f"There have been {self.tickets} tickets issued this period, {paid} of which have been paid. For a total of ${paid * self.price} of revenue.\n")
        

    def spaceCount(self):
        if self.spaces != 0:
            print(f"There are {self.spaces} spaces left.\n")
        else:
            print("There are no more spaces left in this garage.\n")



    def parkCar(self):
        if self.spaces != 0:
            while True:
                user = input("Please enter name for ticket stub\n").lower()
                if user not in self.stubs.keys():
                    self.tickets += 1
                    self.spaces -= 1
                    self.stubs[user] = self.price
                    print(f"Thank you, {user.title()}. You may now proceed to parking.\n")
                    break
                else:
                    print(f"{user} is already in use, please try a different name.\n")
        else:
            print("There are no more parking spaces left in this garage.\n")
        
        

    def pay(self):
        while True:
            for i in self.stubs.keys():
                print(i.title())
            user = input("Please enter user name from list\n").lower()
            if user in self.stubs.keys():
                while True:
                    pay = input(f"Please enter exact change {self.stubs[user]} to continue.\n")
                    if float(pay) == self.stubs[user]:
                        self.stubs[user] = "PAID"
                        self.spaces += 1
                        print(f"{user.title()}, you now have 15 minutes to leave the parking garage. Thank you, have a nice day.\n")
                        break
                    elif pay == "PAID":
                        print("This ticket has already been paid")
                        break        
            break

    
    def garageStatus(self):
        self.ticketCount()
        self.spaceCount()
        print("These are todays tickets:\n")
        for i, j in self.stubs.items():
            print(f"{i.upper()}, {j}")



parking = Garage(0,30, 2.50, {})

def run():
    print("Hello, and welcome to Oop Garage!\n")
    while True:
        action = input("What can our automated services do for you?\n"
                       "Pay\n"
                       "Park\n"
                       "Admin\n"
                       "Quit\n")
        
        if action.lower() == "quit":
            parking.garageStatus()
            break

        elif action.lower() == "pay":
            parking.pay()

        elif action.lower() == "park":
            parking.parkCar()

        elif action.lower() == "admin":
            parking.garageStatus()

        else:
            print(f"{action} is not a valid command. please try again")

run()
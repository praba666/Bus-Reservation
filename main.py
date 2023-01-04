from admin import *
from customer import *
from ticketshow import *

global ch

print("---------------------------------------------------")
print("           Welcome To Murugan Bus Travel        ")
print("---------------------------------------------------")
print()


def start():
    print("1.Admin Registration")
    print("2.Admin Login")
    print()
    adobj = Admin()
    ch = int(input("Enter Your Choice : "))
    if ch == 1:
        adobj.adminregistraion()
    elif ch == 2:
        adobj.adminlogin()
        print()
        print("1.Passengers  Registration")
        print("2. Show Ticket")
        print()
        ch = int(input("Enter Your Choice : "))
        if ch == 1:
            obj = Customdatacsv()
            obj.getcustomerinfo()
            obj.saveinfo()
        elif ch == 2:
            obj = Ticketshow()
            obj.ticket()


start()

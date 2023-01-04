from customer import *


class Ticketshow:
    def ticket(self):
        bln = []
        with open("custom.csv", 'r+', newline="") as f:
            r = csv.reader(f)
            data = list(r)
            id = int(input("Enter the Your Id : "))
            for i in data:
                if id == int(i[0]):
                    for j in i:
                        bln.append(j)
                    break
            else:
                print("Id is Not Available : ")

        print(
            "------------------------------------------------------------------------------")
        print("                          Murugan Bus Travel                               ")
        print(
            "------------------------------------------------------------------------------")
        print()
        print(" e_Ticket :",
              "Salem Address               : Five road, Sakthi complex,Salem")
        print("           ",
              "Phone No\Mob No             : 10000000000,100000000000      ")
        print()
        print("", bln[3], "------------->", bln[4],
              "            ", "        Passenger Id:", bln[0])
        print()
        print(" Passenger Name :",
              bln[1], "              ", "Number of Passenger :", bln[2])
        print(
            "______________________________________________________________________________")
        print()
        print(" Date of Booking :",
              bln[5], "              ", "Seat No :", bln[6], "              ")
        print()
        print(" Bus Type :       ",
              bln[7], "                                                           ")
        print(" Bus Fare :       ",
              bln[8], "                                                           ")
        print()
        print(
            "------------------------------------------------------------------------------")


# obj = Ticketshow()
# obj.ticket()

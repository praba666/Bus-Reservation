import csv


class Customeregistrations():
    def __init__(self):
        self.Name = None
        self.Noofcustomer = None
        self.departure = None
        self.destination = None
        self.ddmmyy = None
        self.seatno = None
        self.selectbustype = None
        self.busfare = None
        self.autoinc = 1
        self.countcol = 0

    def getcustomerinfo(self):
        self.Name = input("Enter the Name : ")
        self.Noofcustomer = int(input("Enter No of Customer : "))
        print("1.Salem")
        print("2.Valappady")
        print("3.Attur")
        print("4.Kallakurichi")

        dl = int(input("Enter the Departur Location : "))
        if dl == 1:
            self.departure = "Salem"
        elif dl == 2:
            self.departure = "Valappady"
        elif dl == 3:
            self.departure = "Attur"
        elif dl == 4:
            self.departure = "Kallakurichi"
        else:
            print("Choose Correct Option")

        print("1.Thambaram")
        print("2.Velachery")
        print("3.Guidy")
        print("4.Chennai")

        dpl = int(input("Enter the Destination Location : "))
        if dpl == 1:
            self.destination = "Thambaram"
        elif dpl == 2:
            self.destination = "Velachery"
        elif dpl == 3:
            self.destination = "Guidy"
        elif dpl == 4:
            self.destination = "Chennai"
        else:
            print("Choose Correct Option")

        self.ddmmyy = input("Journy Date Like 01.01.2023 : ")
        print("[1]__[2]__[3]__[4]__[5]__[6]__[7]__[8]__[9]__[10]")
        print("[11]_[12]_[13]_[14]_[15]_[16]_[17]_[18]_[19]_[20]")
        print("[21]_[22]_[23]_[24]_[25]_[26]_[27]_[28]_[29]_[30]")

        seatnolist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                      16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

        self.bookinglist = []
        while True:
            self.seatno = int(input("Enter the Seat Number : "))
            if self.seatno <= 30:
                if self.seatno in seatnolist:
                    self.bookinglist.append(self.seatno)
                    del seatnolist[self.seatno+1]
                    count = len(seatnolist)
                else:
                    print("Ticket is Already Booked")
                print("Do u want one more seat")
                y = input("Yes or No : ")
                if y == "y":
                    pass
                else:
                    break
            else:
                print("Total Seat Number available in 30 ")

        print("1.AC BUS     FARE=500")
        print("2.NON AC BUS FARE=300")
        self.bustype = int(input("Enter the Bus Type :"))
        if self.bustype == 1:
            self.selectbustype = "AC BUS"
            self.busfare = (self.Noofcustomer*500)
        elif self.bustype == 2:
            self.selectbustype = "NON AC "
            self.busfare = (self.Noofcustomer*300)


class Customdatacsv(Customeregistrations):
    def saveinfo(self):
        try:
            with open("custom.csv", 'r+', newline="") as f:
                r = csv.reader(f)
                data = list(r)
                for i in data:
                    self.autoinc += 1
                    for j in i:
                        self.countcol += 1
                print("Number of Records Found in Database : ", self.autoinc)
        except:
            print("File Has Not Available ")
        finally:
            with open("custom.csv", 'a+', newline="") as f:
                w = csv.writer(f)
                w.writerow([self.autoinc, self.Name, self.Noofcustomer, self.departure,
                           self.destination, self.ddmmyy, self.bookinglist, self.selectbustype, self.busfare])
                print("Data Save Successfully")


# obj = Customdatacsv()
# obj.getcustomerinfo()
# obj.saveinfo()

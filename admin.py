import csv


class Admin:
    def __init__(self):
        self.username = None
        self.password = None

    def adminregistraion(self):
        print("----------------------------------------------------------------")
        print()
        with open("admin.csv", 'w', newline="") as f:
            w = csv.writer(f)
            self.username = input("Enter the user name : ")
            self.password = input("Enter the Password : ")
            w.writerow([self.username, self.password])
            print("Registration successfull")
        print()
        print("----------------------------------------------------------------")

    def adminlogin(self):
        actlist = []
        print("----------------------------------------------------------------")
        print()
        with open("admin.csv", 'r+', newline="") as f:
            r = csv.reader(f)
            data = list(r)
            for i in data:
                for j in i:
                    actlist.append(j)
        while True:
            print("----------------------------------------------------------------")
            print()
            self.username = input("Enter user name :")
            self.password = input("Enter the Password : ")
            if self.username == str(actlist[0]) and self.password == str(actlist[1]):
                print()
                print("Login successfull")
                break
            else:
                print("Invalid username or Password ")

            print("----------------------------------------------------------------")
            print()


# obj = Admin()
# # obj.adminregistraion()
# obj.adminlogin()

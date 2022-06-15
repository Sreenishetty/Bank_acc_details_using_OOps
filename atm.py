# ATM Program

from Bank_acc_details import *
import random


# This method is called in the bank_acc_details.py file for abstract method
# This is a another example to demonstrate the working of abstaract method
def accessing():
    print("")
    print("Welcome to State bank of India")
    p = random.randint(0,5)
    m = 250000
    if(p == p):
        print("1 -> Withdraw")
        print("2 -> Balance Enquiry")
        print("3 -> Fast Cash")
        c = int(input("Please choose transactions: "))
        if (c == 1):
            w=int(input("Enter withdraw amount: "))
            if (w < m):
                print("Please take your amount:", w)
            else:
                print("Invalid cash")

        elif(c==2):
            print("Your available amount : ",m)

        elif (c == 3):
            print("Please Enter 1 for to withdraw Rs.5000")
            print("Please Enter 2 for to withdraw Rs.10000")
            print("Please Enter 3 for to withdraw Rs.15000")
            print("Please Enter 4 for to withdraw Rs.20000")
            f = int(input("Enter fast cash option: "))
            if (f == 1):
                print("Please take cash 5000")
            elif (f == 2):
                print("Please take cash 10000")
            elif (f == 3):
                print("Please take cash 15000")
            elif (f == 4):
                print("Please take cash 20000")
            else:
                print("Invalid fast cash option")
        else:
            print("Wrong choice")
        
    else:
        print("Wrong pin number")

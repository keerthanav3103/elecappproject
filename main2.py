import sys
sys.path.append(r'C:\Users\My Pc\Desktop\electronic appliance project\mypackage')
import Bea
import Cea
import json

while True:
    print("WELCOME TO ELECTRONICS CARE")
    print('Do you want to\n1.View Appliances\n2.Cancel Order\n3.Exit')
    choice=int(input())
    if choice==1:
        print("please enter your name ")
        strval=input().strip()
        Bea.bookingappliance(strval)
    elif choice==2:
        getref=int(input('Referid: '))
        Cea.cancellingappliance(getref)
    elif choice==3:
        quit()
    else:
        print("Invalid choice")
        print("Please enter the correct choice")

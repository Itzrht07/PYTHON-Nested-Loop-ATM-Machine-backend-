#_________________________________________________DETAILED STRUCTURE_____________________________
print("welcome to RINKI BANK ATM")
restart=("y")
chance=3
balance=500

#________________________________________________________PIN ENTER & (4) OPTIONS_________________
while chance>=0:
    pin=int(input("enter the pin:"))
    if pin==(1234):
        print("you enter the right pin \n")
        while restart not in ("n","no","N","NO"):
            print("1 for balance enquiry")
            print("2 for withdrawl")
            print("3 pay in")
            print("4 to return card")
            option =int(input("\nchoose an optioin:"))

#___________________________________________________________________FOR OPTION 1_________________
            if option == 1:
                print("your current balance is:",balance)
                restart=input("\nfor main meny press (y):")
                if restart in ("n","no","N","NO"):
                    print("DHANYAWAD")
                    break

#___________________________________________________________________FOR OPTION 2_________________
            elif option==2:
                withdrawl=float(input("enter withdrawl amount:"))
                withdrawl=balance-withdrawl
                print("\n your current balance is\n:",withdrawl)
                restart=input("\nfor main menu press (y):")
                if restart in ("n","no","N","NO"):
                    print("DHANYAWAD")
                    break

#____________________________________________________________________FOR OPTION 3________________
            elif option==3:
                payin=float(input("enter the amount you want to payin:"))
                payin=balance+payin
                print("\nyour current balance  is:\n",payin)
                restart=input("\nfor main menu press (y):")
                if restart in ("n","no","N","NO"):
                    print("DHANYAWAD")
                    break
#_____________________________________________________________________FOR OPTION 4_______________
            elif option==4:
                print("wait for 5 seconds")
                a=1
                while (a<=5):
                    print(a)
                    a=a+1
                print("DHANYAWAD")
                break
            break
        break

#______________________________________________________________________ATM PIN 3 CHANCES_________
    elif pin != ("1234"):
        print("incorrect password")
        chance=chance-1
        if chance==0:
            print("\n TOO MANY TRIES CARD FAILED")
            break
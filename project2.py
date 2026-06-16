#ATM Machine System
balance = 10000
correctpin = 1234

PIN = int(input("Enter the PIN:"))
if PIN == correctpin :
    print("\n Welcome to ATM")
    while True:
        print("choose any one:")
        print("1.Check Balance")
        print("2.Deposite Money")
        print("3.Withdraw Money")
        print("4.Exit")

        choice = int(input("Enter Your Choice(1to4)"))

        if choice == 1:
            print("your balance is:", balance)
        elif choice == 2:
            amount = float(input("enter the amount:"))
            if amount>0:
                balance += amount
                print(f"{amount} is deposite successfully.")
                print("your current balance is:" , balance)
            else:
                print("invalid amount")
        
        elif choice == 3:
            amount= int(input("enter amount to withdraw:"))
            if amount < 0 :
                print("invalid")
            elif amount > balance:
                print("insufficient balance")
            else:
                 balance -= amount
                 print(f"{amount} is withdraw successfully.")
                 print("your current balance is :" , balance)
        else:
            print("Thank You")
else:
    print("incorrect PIN")



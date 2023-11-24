import random

def choice():
    print("Please register with one of the following banks:")
    print("1-SBI, 2-PNB, 3-UNION, 4-Exit")
    x = int(input("Choose: "))
    return x

def register(choice):
    if choice == 1:
        print("Welcome to SBI. Please register.")
        a = input("Please enter 'yes' if already registered, otherwise 'no': ")
        if a == "yes":
            print("1-withdrawl ")
            print("2-check balance ")
            print("3-deposite ")
            print("4-exit ")
                
            y = int(input("Enter your choice:"))
            if y == 1:
                pin = int(input("Enter your PIN: "))
                amount=int(input("Please enter the withdrawal amount"))
                account_number=int(input("Please enter the account number"))

                 
                if account_number>999999 or account_number<100000:
                      
                       print("Invalid Pin")
                       
                else:
                    cvv_number=int(input("Please enter the cvv number"))
                     
                                                         
                
                
                print("THANK YOU VISIT AGAIN")
            elif y == 2:
                pin = int(input("Enter your PIN: "))
                account_number=int(input("Please enter the account number"))
                cvv_number=int(input("Please enter the cvv number"))
                print("Your balance is ........")
                print("THANK YOU VISIT AGAIN")
                
            elif y == 3:
                pin = int(input("Enter your PIN: "))
                print("Please enter the deposit amount")
            elif y == 4:
                print("Visit again")
        elif a == "no":
            print("Please Register")
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            accno = random.randint(100000, 999999)  # Generate a random 6-digit account number
            cvv= random.randint(100, 999)

            if age < 18:
                print("You are not eligible for an account with SBI")
            else:
                print("Your account has been created with the following details:")
                print(f"Name: {name}")
                print(f"Age: {age}")
                print(f"Account Number: {accno}")
                print(f"Cvv Number: {cvv}")
                print("Please remember these details for future reference.")
    elif choice == 2:
      
        print("Welcome to PNB. Please register.")
        a = input("Please enter 'yes' if already registered, otherwise 'no': ")
        if a == "yes":
            print("1-withdrawl ")
            print("2-check balance ")
            print("3-deposite ")
            print("4-exit ")
                
            y = int(input("Enter your choice:"))
            if y == 1:
                pin = int(input("Enter your PIN: "))
                print("Please enter the withdrawal amount")
            elif y == 2:
                pin = int(input("Enter your PIN: "))
                print("Your balance is ........")
            elif y == 3:
                pin = int(input("Enter your PIN: "))
                print("Please enter the deposit amount")
            elif y == 4:
                print("Visit again")
        elif a == "no":
            print("Please Register")
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            accno = random.randint(100000, 999999)  # Generate a random 6-digit account number
            cvv= random.randint(100, 999)

            if age < 18:
                print("You are not eligible for an account with SBI")
            else:
                print("Your account has been created with the following details:")
                print(f"Name: {name}")
                print(f"Age: {age}")
                print(f"Account Number: {accno}")
                print(f"Cvv Number: {cvv}")
                print("Please remember these details for future reference.")
    elif choice == 3:
        
        print("Welcome to UNION. Please register.")
        a = input("Please enter 'yes' if already registered, otherwise 'no': ")
        if a == "yes":
            print("1-withdrawl ")
            print("2-check balance ")
            print("3-deposite ")
            print("4-exit ")
                
            y = int(input("Enter your choice:"))
            if y == 1:
                pin = int(input("Enter your PIN: "))
                print("Please enter the withdrawal amount")
            elif y == 2:
                pin = int(input("Enter your PIN: "))
                print("Your balance is ........")
            elif y == 3:
                pin = int(input("Enter your PIN: "))
                print("Please enter the deposit amount")
            elif y == 4:
                print("Visit again")
        elif a == "no":
            print("Please Register")
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            accno = random.randint(100000, 999999)  # Generate a random 6-digit account number
            cvv= random.randint(100, 999)

            if age < 18:
                print("You are not eligible for an account with SBI")
            else:
                print("Your account has been created with the following details:")
                print(f"Name: {name}")
                print(f"Age: {age}")
                print(f"Account Number: {accno}")
                print("Please remember these details for future reference.")
    elif choice == 4:
        print("Thank you for using our service.")
       
    else:
        print("Wrong input")
        


# Call the choice function and then the register function
selected_bank = choice()
register(selected_bank)

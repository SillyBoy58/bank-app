import time
import random
import json

def enter_info(what_is_needed):
    prompt = ''
    
    if what_is_needed.lower() == "name":
        prompt = 'name'
    else:
        prompt = "last name"


    while True:
        word = input(f"Enter your {prompt}: ")
        if word.isalpha():
            word = word.capitalize()
            break
        print("Your input can only be made out of letters!")

    return word

def check_balance():
    print(f"Your balance is: {bank_balance} {bank_currency}")
    time.sleep(2.5)
    ReturnToMain()

def putIn_money():
    global bank_balance
    while True:
        amount = input("How much money would you like to add?: ")
        if amount.isnumeric():
            amount = float(amount)
            break
        print("Only numbers are accepted!")
    
    bank_balance += amount
    print(f"You successfully added {amount} euros")
    
def withdraw_money():
    global bank_balance
    while True:
        amount = input("How much money would you like to withdraw?: ")
        if amount.isnumeric():
            amount = float(amount)
            break
        print("Only numbers are accepted!")
    
    bank_balance -= amount
    print(f"You successfully withdrawed {amount} euros")

def change_name():
    global bank_balance
    global username
    global user_last_name

    Choosing = input("This action will cost 50 euros. Are you sure?:\n1. Yes\n2. No: ")
    if Choosing == "1":
        username = enter_info("name")
        user_last_name = enter_info("last name")
        bank_balance -= 50
    else:
        main()
    
def invest():
    global bank_balance
    global bank_currency

    while True:
        choice = input("Choose how you want to invest:\n1. Cryptocurrency (high risk)\n2. Shares (medium risk)\n3. Return: ")
        Chance = random.randint(1, 100)

        if choice == "1" or choice == "2":
            Money_to_invest = float(input("How much would you like to invest?: "))
            if bank_balance >= Money_to_invest:
                if choice == "1":
                    if Chance <= 35:
                        bank_balance -= Money_to_invest
                        Money_to_invest *= 3
                        bank_balance += Money_to_invest
                        print("You successfuly tripled your invested money!")
                        print(f"Your current balance:{bank_balance} {bank_currency}")
                    
                    elif Chance >= 35:
                        bank_balance -= Money_to_invest
                        Money_to_invest = 0
                        print("All of your money dissapeared! :c")
                        print("99% of gamblers quit right before winning, try again!")
                        print(f"Your current balance:{bank_balance} {bank_currency}")
                    
                    else:
                        print("You don't have that much money!")

                elif choice == "2":
                    if Chance <= 50:
                        bank_balance -= Money_to_invest
                        Money_to_invest *= 2
                        bank_balance += Money_to_invest
                        print("You successfuly doubled your invested money!")
                        print(f"Your current balance:{bank_balance} {bank_currency}")
                    
                    elif Chance >= 50:
                        bank_balance -= Money_to_invest
                        Money_to_invest = 0
                        print("All of your money dissapeared! :c")
                        print("99% of gamblers quit right before winning, try again!")
                        print(f"Your current balance:{bank_balance} {bank_currency}")
            else:
                print("You don't have that much money!")
        
        elif choice == "3":
            ReturnToMain()
        
        else:
            print("Invalid input! (Only numbers from 1-3 are accepted)")
        
def ReturnToMain():
    main()

def CurrentExchange():
    global bank_balance
    global bank_currency

    opened_file= open('/home/subbywubbydubdub/Documents/VSCode/Pamokoms/Pamokoms/1 Trimestras/Projektas/currencies.json')
    currencies = json.load(opened_file)
    opened_file.close

    while True:
        current_currency = bank_currency
        ChangeInto = input("What currency would you like to convert to? \nAvailible are:\nEUR\nUSD\nGBP\nAUD\nJPY: ")
        if ChangeInto in currencies:
            if ChangeInto == bank_currency:
                print("Your currency is already that!")
                time.sleep(1)
            else:
                bank_balance = bank_balance * currencies[current_currency][ChangeInto]
                bank_currency = ChangeInto
                print(f"Your current balance: {bank_balance} {bank_currency}")
                ReturnToMain()
        else: 
            print("Select a valid currency!")


bank_balance = 100
bank_currency = "EUR"
username = enter_info("name")
user_last_name = enter_info("last name")

def main():
    while True:
        choice = input(f"Dear {username} {user_last_name}, choose:\n1. Check your balance. \n2. Put in money. \n3. Withdraw money. \n4. Change name and last name. \n5. Invest. \n6. Convert your currency \n7. Quit: ")
        
        match choice:
            case "1":
                check_balance()
            case "2":
                putIn_money()
            case "3":
                withdraw_money()
            case "4":
                change_name()
            case "5":
                invest()
            case "6":
                CurrentExchange()
            case "7":
                exit()

if __name__ == "__main__":
    main()
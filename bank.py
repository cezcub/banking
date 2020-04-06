import string
from random import choice
import time
import json
from accounts import Account, Checking, Savings
import constants

nums = []
mylist = []
usernames = []

# Read file for account info
with open(constants.filename , "r") as file2:
        length = len(file2.readlines())
        file2.seek(0)
        for i in range(length):
            mylist.append(json.loads(file2.readline().strip("\n")))
for i in mylist:
    nums.append(i["account_number"])
for i in mylist:
    usernames.append(i["username"])

action = input("Would you like to open a checking account, open a savings account, or acess an existing account? Please select 1,2,or 3): ").strip()

if action == "1":
    # Ask for info to set up account
    name = input("What is your full name?: ").title().strip()
    phone_number = input(
        "What is your phone number? (Please enter as xxxxxxxxx): ")
    # Generate random account number
    while True:
        number = ''.join(choice(string.digits) for i in range(10))
        if number not in nums:
            account_number = number
            break
        else:
            continue
    balance = float(input(
        "How much money would you like to deposit? (Please enter as a number): ").strip())
    print("Your account number is " + account_number)
    # Check for unique username
    while True:
        the_username = input("What would you like your username to be?: ")
        if the_username not in usernames:
            username = the_username
            break
        else:
            print("Sorry, that username is already taken.")
            continue
    password = input("What would you like your password to be?: ")
    # Initalize account and write to file
    my_object = Checking(name, balance,  account_number,
                         username, password, phone_number, constants.accounttype1, constants.overdraft)
    with open(constants.filename, "a") as f:
        f.write(json.dumps(vars(my_object)) + "\n")
    print("We have succesfully set up your account!")

elif action == "2":
    # Check if they want to continue
    while True:
        check = input(
            "Our interest rate is 1% per year. Would you like to continue?: ").strip().title()
        if check == "Yes":
            # Ask for info to set up account
            name = input("What is your full name?: ").title().strip()
            phone_number = input(
                "What is your phone number? (Please enter as xxx-xxx-xxx): ")
            # Generate random account number
            while True:
                number = ''.join(choice(string.digits) for i in range(10))
                if number not in nums:
                    account_number = number
                    break
                else:
                    continue
            balance = float(input(
                "How much money would you like to deposit? (Please enter as a number): ").strip())
            # Check for unique username
            while True:
                the_username = input("What would you like your username to be?: ")
                if the_username not in usernames:
                    username = the_username
                    break
                else:
                    print("Sorry, that username is already taken.")
                    continue
            password = input("What would you like your password to be?: ")

            # Initalize account and write to file
            my_other_object = Savings(
                name, balance, account_number, username, password, phone_number, constants.accounttype2, 0, time.localtime())

            with open(constants.filename, "a") as file:
                file.write(json.dumps(vars(my_other_object)) + "\n")

            print("We have succesfully set up your account!")
            break
        elif check == "No":
            print("Ok, have a good day!")
            break
        else:
            print("I'm sorry, I didn't understand that. Please answer yes or no.")
            continue

elif action == "3":
    mynewlist = []
    mynewerlist = []
    yetanotherlist = []

    # Initailize dicts into objects
    for i in mylist:
        if i["account_type"] == "Checking":
            mynewlist.append(Checking(**i))
        elif i["account_type"] == "Savings":
            mynewlist.append(Savings(**i))
        else:
            raise "Unknown account type"
    # Check login info
    while True:
        username_check = input("What is your username?: ")
        for i in mynewlist:
            if i.username == username_check:
                mynewerlist.append(i)
        password_check = input("What is your password?: ")
        for i in mynewerlist:
            if i.password == password_check:
                print("Login successful!")
                yetanotherlist.append(i)
                break
        else:
            option = input("Login was unseccessful. Would you like to try again?: ").strip().title()
            if option[0] == "Y":
                continue
            else:
                print("Okay, have a nice day!")
                break
        
        # If saving account, pay interest
        if len(vars(yetanotherlist[0])) == 8:
            yetanotherlist[0].pay_interest()
        yetanotherlist[0].statement()
        
        # Take and perform deposit/withdrawal
        action2 = input("Would you like to make a deposit, or make a withdrawal? (Please enter 1 or 2): ").strip()
        if action2 == "1":
            amount_number = int(input("How much would you like to deposit? (Please enter as a number): ").strip())
            yetanotherlist[0].deposit(amount_number)
            yetanotherlist[0].statement()
        elif action2 == "2":
            amount_number = int(input("How much would you like to withdraw? (Please enter as a number): ").strip())
            yetanotherlist[0].withdraw(amount_number)
            yetanotherlist[0].statement()
        print("Have a good day!")
        break 
    # Write to file
    with open(constants.filename, "w") as the_last_step:
        for i in mylist:
            the_last_step.write(json.dumps(i) + "\n")
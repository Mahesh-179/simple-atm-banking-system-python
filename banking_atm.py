import time
user_name = input("Enter your user_name: ")
password_user = int(input("Enter your password_user: "))

if user_name == "admin" and password_user == 1234:
    print("Logging in...")
    time.sleep(1)
    print("✅ Login Successful, Welcome to our prestigious ATM System")
else:
    print(f"❌ Sorry, {user_name} not found.")
    quit()

# total_balance
available_balance = 1000

# declaring the user panel
print("\n Here is a list of all your bank services:")
print(" 1.To Check Available Balance\n 2.To Deposit\n 3.To Withdraw\n 4.To Cancel")

user_response = int(input("Enter your choice (1-4):- "))
time.sleep(0.5)

if user_response == 1:
    print("Fetching your balance...")
    time.sleep(1)
    print(f"Your Available Balance is NPR {available_balance}")

elif user_response == 2:
    user_deposit = int(input("Enter the amount you want to deposit: "))
    print("Processing deposit...")
    time.sleep(1)
    available_balance += user_deposit
    print(f" NPR {user_deposit} deposited successfully")
    print(f"Your total balance is NPR {available_balance}")

elif user_response == 3:
    user_withdraw = int(input("Enter the amount you want to withdraw: "))
    print("Processing withdrawal...")
    time.sleep(1)
    if user_withdraw>available_balance:
        print("You don't have enough money")
    elif user_withdraw<available_balance:
        available_balance -= user_withdraw
        print(f"NPR {user_withdraw} withdrawn successfully")
        print(f"Your total balance is NPR {available_balance}")

elif user_response == 4:
    print("Cancelling transaction...")
    time.sleep(1)
    print("Thank you for using our prestigious ATM System")
    quit()

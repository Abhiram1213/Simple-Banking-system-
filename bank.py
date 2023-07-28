def deposit(account_number):
    amount = float(input("Enter amount to deposit: "))
    accounts[account_number]["balance"] += amount
    print(f"Amount {amount} deposited. New balance: {accounts[account_number]['balance']}")

def withdraw(account_number):
    amount = float(input("Enter amount to withdraw: "))
    if accounts[account_number]["balance"] >= amount:
        accounts[account_number]["balance"] -= amount
        print(f"Amount {amount} withdrawn. New balance: {accounts[account_number]['balance']}")
    else:
        print("Insufficient funds.")

def bank():
    account_number = login()
    if account_number is not None:
        while True:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                deposit(account_number)
            elif choice == "2":
                withdraw(account_number)
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

bank()
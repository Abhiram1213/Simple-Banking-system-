This Python script implements a simple banking system where users can log in, deposit money, withdraw money, and check their account balance. The banking system is represented by a dictionary named bank_data, where each key is an account number and its corresponding value is a dictionary containing the account's PIN and balance. The user interacts with the system through the console.

bank_data Dictionary:

This dictionary stores account information for users. Each account is identified by a unique account number (key), and the value associated with each key is another dictionary with the following key-value pairs: "pin": The PIN associated with the account. "balance": The current balance in the account. login() Function:

This function is responsible for handling the login process. It prompts the user to enter their account number and PIN. If the entered account number and PIN match an existing account in bank_data, the user is considered logged in, and their account number is returned. If the login is unsuccessful (invalid account number or incorrect PIN), the function returns None. deposit(account_number) Function:

This function allows a logged-in user to deposit money into their account. It prompts the user to enter the amount they want to deposit. If the amount is valid (greater than zero), it adds the amount to the user's account balance and displays the updated balance. If the amount is invalid (less than or equal to zero), it informs the user that the deposit amount should be greater than zero. withdraw(account_number) Function:

This function allows a logged-in user to withdraw money from their account. It prompts the user to enter the amount they want to withdraw. If the amount is valid (greater than zero and less than or equal to the account balance), it deducts the amount from the user's account balance and displays the updated balance. If the amount is invalid (less than or equal to zero or greater than the account balance), it informs the user of the withdrawal rules. print_banking_system() Function:

This function serves as the main entry point for the banking system. It displays a welcome message and then calls the login() function to authenticate the user. If the login is successful, it displays a menu of options to the user (Deposit, Withdraw, Check Balance, and Logout). The user can choose an option by entering the corresponding number, and the selected action is performed. The user can log out at any time by selecting the "Logout" option. name == "main":

This block of code is executed only if the script is run directly (not imported as a module). It calls the print_banking_system() function to start the banking system.

import datetime

accounts = {}
admins = {"admin": "admin123"}
next_account_number = 1001

def save_data_to_file():
    with open("bank_data.txt", "w") as file:
        for acc_no, info in accounts.items():
            file.write(f"Account Number: {acc_no}\t")
            file.write(f"Holder: {info['name']}\t")
            file.write(f"Balance: {info['balance']}\t")
            file.write("Transactions:\t")
            for transaction in info['transactions']:
                file.write(f"{transaction}\t")
            file.write("\n")

# ------------------- Admin Functions -------------------

def create_admin_account():
    username = input("Enter new admin username: ").strip()
    if username in admins:
        print("Admin username already exists.")
        return
    password = input("Enter new admin password: ").strip()
    admins[username] = password
    print("Admin account created successfully!")

def admin_login():
    username = input("Enter admin username: ").strip()
    password = input("Enter admin password: ").strip()
    if username in admins and admins[username] == password:
        print("Login successful!")
        return True
    print("Invalid credentials. Access denied.")
    return False

def view_users_transaction_history():
    if not accounts:
        print("No user accounts found.")
        return
    for acc_no, info in accounts.items():
        print(f"\nAccount Number: {acc_no}")
        print(f"Holder Name: {info['name']}")
        print("Transactions:")
        for t in info["transactions"]:
            print(f"  {t}")

def admin_panel():
    while True:
        print("\n--- Admin Panel ---")
        print("1. Create Admin Account")
        print("2. Create User Account")
        print("3. View Users' Transaction History")
        print("4. Exit Admin Panel")

        choice = input("Enter choice: ")
        if choice == '1':
            create_admin_account()
        elif choice == '2':
            create_account()
        elif choice == '3':
            view_users_transaction_history()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

# ------------------- User Functions -------------------

def create_account():
    global next_account_number
    name = input("Enter account holder name: ").strip()
    password = input("Set a password for this account: ").strip()
    try:
        initial_balance = float(input("Enter initial balance: "))
        if initial_balance < 0:
            print("Initial balance cannot be negative.")
            return
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    account_number = str(next_account_number)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    accounts[account_number] = {
        "name": name,
        "password": password,
        "balance": initial_balance,
        "transactions": [f"{timestamp} - Account created with {initial_balance}"]
    }
    next_account_number += 1
    save_data_to_file()
    print(f"Account created successfully! Your account number is: {account_number}")

def deposit(acc_no=None):
    if not acc_no:
        acc_no = input("Enter account number: ").strip()
    if acc_no not in accounts:
        print("Account not found.")
        return
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount.")
        return
    accounts[acc_no]["balance"] += amount
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    accounts[acc_no]["transactions"].append(f"{timestamp} - Deposited {amount}")
    save_data_to_file()
    print("Deposit successful.")

def withdraw(acc_no=None):
    if not acc_no:
        acc_no = input("Enter account number: ").strip()
    if acc_no not in accounts:
        print("Account not found.")
        return
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount.")
        return
    if amount > accounts[acc_no]["balance"]:
        print("Insufficient balance.")
        return
    accounts[acc_no]["balance"] -= amount
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    accounts[acc_no]["transactions"].append(f"{timestamp} - Withdrawn {amount}")
    save_data_to_file()
    print("Withdrawal successful.")

def view_account(acc_no=None):
    if not acc_no:
        acc_no = input("Enter account number: ").strip()
    if acc_no not in accounts:
        print("Account not found.")
        return
    info = accounts[acc_no]
    print(f"Account Number: {acc_no}")
    print(f"Holder Name: {info['name']}")
    print(f"Balance: {info['balance']}")
    print("Transactions:")
    for t in info["transactions"]:
        print(f"  {t}")

def user_panel():
    acc_no = input("Enter your account number: ").strip()
    if acc_no not in accounts:
        print("Account not found.")
        return

    password = input("Enter your password: ").strip()
    if accounts[acc_no]["password"] != password:
        print("Incorrect password.")
        return

    while True:
        balance = accounts[acc_no]["balance"]
        print(f"\n--- User Panel (Account: {acc_no}, Balance: {balance}) ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Account")
        print("4. Exit User Panel")

        choice = input("Enter choice: ")
        if choice == '1':
            deposit(acc_no)
        elif choice == '2':
            withdraw(acc_no)
        elif choice == '3':
            view_account(acc_no)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

# ------------------- Main Menu -------------------

def main_menu():
    while True:
        print("\n--- Welcome to SK Shine Bank ---")
        print("1. Admin Login")
        print("2. User Panel")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            if admin_login():
                admin_panel()
        elif choice == '2':
            user_panel()
        elif choice == '3':
            save_data_to_file()
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


main_menu()

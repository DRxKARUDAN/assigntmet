






from datetime import datetime
accounts = {}
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

def create_account():
    global next_account_number
    name = input("Enter account holder name: ").strip()
    try:
        initial_balance = float(input("Enter initial balance: "))
        if initial_balance < 0:
            print("Initial balance cannot be negative.")
            return
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    account_number = str(next_account_number)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    accounts[account_number] = {
        "name": name,
        "balance": initial_balance,
        "transactions": [f"{timestamp} - Account created with {initial_balance}"]
    }
    next_account_number += 1
    print(f"Account created successfully! Your account number is: {account_number}")

def deposit():
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
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    accounts[acc_no]["transactions"].append(f"{timestamp} - Deposited {amount}")
    print("Deposit successful.")

def withdraw():
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
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    accounts[acc_no]["transactions"].append(f"{timestamp} - Withdrawn {amount}")
    print("Withdrawal successful.")

def view_account():
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
        print(f" {t}")

def main_menu():
    while True:
        print("\n--- Mini Banking App ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Account")
        print("5. Save and Exit")

        choice = input("Enter choice: ")
        if choice == '1':
            create_account()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            view_account()
        elif choice == '5':
            save_data_to_file()
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
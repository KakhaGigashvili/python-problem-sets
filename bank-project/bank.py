from datetime import datetime
import getpass
import json 
import os 

DB_FILE = "db.json"

def load_db():
    if not os.path.exists(DB_FILE):
        return {"users": {}}
    with open(DB_FILE, "r") as f:
        return json.load(f)
    


def save_db(db):
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=2)



def register():
    username = input("Choose a username: ").strip()
    if not username:
        print("Username cannot be empty")
        return
    db = load_db()
    if username in db["users"]:
        print("Username is already taken.")
        return
    password = getpass.getpass("Choose a password: ")
    if not password:
        print("Password cannot be empty.")
        return
    db["users"][username] = {
        "password": password,
        "balance": 0.0,
        "transactions": [],
    }
    save_db(db)
    print(f"Account created for '{username}'")



def login():
    username = input("Username: ").strip()
    password = getpass.getpass("password: ")
    db = load_db()
    user = db["users"].get(username)
    if user is None or user["password"] != password:
        print("Invalid username or passwrd")
        return None
    print(f"Welcome back, {username}")
    return username

def show_balance(username):
    db = load_db()
    print(f"Current balance: ${db["users"][username]["balance"]:.2f}")
    
def read_amount(prompt):
    raw = input(prompt).strip()
    try:
        amount = float(raw)
    except ValueError:
        print("That's not valid number.")
        return None
    if amount <= 0:
        print("Amount must be greater thant zero")
        return None
    return round(amount, 2)


def add_transaction(user, entry):
    user["transactions"].append(
    {
        **entry,
        "at": datetime.now().isoformat(timespec="seconds")
    })

def deposit(username):
    amount = read_amount("Amount to deposut: $")
    if amount is None:
        return
    db = load_db()
    user = db["users"][username]
    user["balance"] += amount
    add_transaction(
        user, 
        {
            "type": "deposit",
            "amount": amount,
        })
    save_db(db)
    print(f"Deposited ${amount:.2f}. New balance: ${user["balance"]}")

def withdraw(username):
    amount = read_amount("Ammount to withdraw: $")
    if amount is None:
        return
    db = load_db()
    user = db['users'][username]
    if user["balance"] < amount:
        print("Insifficient funds.")
        return
    user["balance"] -= amount
    add_transaction(user, {"type": "withraw", "amount": amount})
    save_db(db)
    print(f"Withdrew ${amount:.2f}. New balance: ${user['balance']}")

def transfer(username):
    recipient = input("Recipient username: ").strip()
    db = load_db()
    if recipient not in db["users"]:
        print("That user does not exist.")
    if recipient == username:
        print("print you cannot transfer to yourself")
        return
    amount = read_amount("Amount to transfer: $")
    if amount is None:
        return
    sender = db["users"][username]
    if sender["balance"] < amount:
        print("Insufficient funds.")
        return
    receiver = db["users"][recipient]
    sender["balance"] -= amount
    receiver["balance"] += amount
    add_transaction(sender, {"type": "transfer_out", "amount": amount, "to": recipient})
    add_transaction(receiver, {"type": "transfer_in", "amount": amount, "from": username})
    save_db(db)
    print(f"Transferred ${amount:.2f} to {recipient}. New balance ${sender['balance']:.2f}")

def show_history(username):
    db = load_db()
    txs = db["users"][username]["transactions"]
    if not txs:
        print("No transactions yet.")
        return
    print("\n--- Transactions History ---")
    for t in txs:
        line = f"[{t['at']}] {t['type']:<13} ${t['amount']:.2f}"
        if "to" in t:
            line += f" -> {t['to']}"
        if "from" in t:
            line += f" <- {t['from']}"
        print(line)

def user_menu(username):
    while True:
        print(f"\n --- loggined in as {username} ---")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction history")
        print("6. Logout")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            show_balance(username)
        elif choice == "2":
            deposit(username)
        elif choice == "3":
            withdraw(username)
        elif choice == "4":
            transfer(username)
        elif choice =="5":
            show_history(username)
        elif choice == "6":
            print("Logged out.")
            return
        else:
            print("Invalid choice.")



def main():
    while True:
        print("\n === Simple Bank ===")
        print("1. Register")
        print("2. Login")
        print("3. Quit")
        choice = input("Choice an option: ").strip()
        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                user_menu(user)
        elif choice == "3":
            print("Goodbye!")
            return
        else:
            print("Invalid choice")
            


if __name__ == "__main__":
    main()
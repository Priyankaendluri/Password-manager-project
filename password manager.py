from cryptography.fernet import Fernet
import os
import getpass

# ----- Step 1: Generate/load key -----
def load_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
    return key

key = load_key()
fernet = Fernet(key)

# ----- Step 2: Save Password -----
def add_password():
    name = input("Account Name: ")
    username = input("Username/Email: ")
    password = getpass.getpass("Password: ")
    
    with open("passwords.txt", "a") as f:
        enc_pass = fernet.encrypt(password.encode()).decode()
        f.write(f"{name} | {username} | {enc_pass}\n")
    print("Password saved successfully!")

# ----- Step 3: View Passwords -----
def view_passwords():
    if not os.path.exists("passwords.txt"):
        print("No passwords stored yet.")
        return

    with open("passwords.txt", "r") as f:
        for line in f:
            name, username, enc_pass = line.strip().split(" | ")
            dec_pass = fernet.decrypt(enc_pass.encode()).decode()
            print(f"Account: {name}\n  Username: {username}\n  Password: {dec_pass}\n")

# ----- Step 4: Main Menu -----
def main():
    while True:
        print("\nPASSWORD MANAGER")
        print("1. Add New Password")
        print("2. View Saved Passwords")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()


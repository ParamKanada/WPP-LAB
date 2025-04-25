class PasswordManager:
    def __init__(self):
        self.oldpasswords = []  #list to store old passwords

    def get_password(self):
        if len(self.oldpasswords) >0:
            return self.oldpasswords[-1]
        else:
            return None
    
    def set_password(self,new_password):
        if new_password not in self.oldpasswords:
            self.oldpasswords.append(new_password)
        else:
            print("This passwords already used before, try another one.")

    def is_correct(self,password):
        if password==self.oldpasswords[-1]:
            print("Correct Password")
        else:
            print("Wrong password")

my_passwordmanager=PasswordManager()

while True:
    print("\n1. Set Password")
    print("2. Get Current Password")
    print("3. Check Password")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        new_password = input("Enter new password: ")
        my_passwordmanager.set_password(new_password)

    elif choice == '2':
        print("Current password:", my_passwordmanager.get_password())

    elif choice == '3':
        check_password = input("Enter password to check: ")
        if my_passwordmanager.is_correct(check_password):
            print("Password is correct.")
        else:
            print("Password is incorrect.")

    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
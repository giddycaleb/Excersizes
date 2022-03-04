class User:
    def __init__(self, first_name, last_name, gender, street_address, city, email, cc_number, cc_type, balance,
                 account_no):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.street_address = street_address
        self.city = city
        self.email = email
        self.cc_number = cc_number
        self.cc_type = cc_type
        self.balance = balance
        self.account_no = account_no
        userList.append(self)

    def displayInfo(self):
        print("First Name: {}\n"
              "Last Name: {}\n"
              "Gender: {}\n"
              "Address: {}\n"
              "City: {}\n"
              "Email: {}\n"
              "CC Number: {}\n"
              "CC Type: {}\n"
              "Balance: {}\n"
              "Account Number: {}".format(self.first_name, self.last_name,
                                          self.street_address, self.city, self.email,
                                          self.cc_number, self.cc_type, self.balance, self.account_no))

    def change_balance(self, balance):
        self.balance = balance


def generateUsers():
    import csv
    with open('bankUsers.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
        for line in filereader:
            User(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], float(line[8][1:]), line[9])


def findUser():
    user_found = True
    while user_found:
        user_to_find = input("Please input a User you would like to find: ").upper()
        for user in userList:
            if user.first_name.upper() == user_to_find or user.last_name.upper() == user_to_find:
                print(f"Hi {user.first_name}")
                print(f"Balance: {user.balance}")
                return user
                user_found = False
        if user_found:
            print("Sorry No User was found with that name.")


def overdrafts():
    overdraft_list = []
    overdraft_total = 0
    for user in userList:
        if user.balance < 0:
            overdraft_list.append([user.first_name, user.last_name])
            overdraft_total = overdraft_total - user.balance

    print(f"People with overdraft accounts: \n")
    for user in overdraft_list:
        print(user)
    print(f"Amount of Overdraft accounts: {len(overdraft_list)}\n"
          f"Total Amount owed: {round(overdraft_total, 2)}")


def missingEmails():
    missemail_list = []
    for user in userList:
        if user.email == "":
            missemail_list.append([user.first_name, user.last_name])
    print(f"People with no E-Mail: \n")
    for user in missemail_list:
        print(user)
    print(f"Total Amount with No E-Mail: {len(missemail_list)}")


def bankDetails():
    total_bal = 0
    high_user = ["", 0]
    low_user = ["", 0]
    for user in userList:
        total_bal += user.balance
        if user.balance >= high_user[1]:
            high_user = [f"{user.first_name} {user.last_name}", user.balance]
        if user.balance <= low_user[1]:
            low_user = [f"{user.first_name} {user.last_name}", user.balance]
    print(f"Total Users: {len(userList)}\n"
          f"Total Balance: {round(total_bal, 2)}\n"
          f"User With Highest Balance: {high_user[0]} with ${high_user[1]}\n"
          f"User With Lowest Balance: {low_user[0]} with ${low_user[1]}")


def transfer():
    acc_found = False
    acc_receive = False
    while not acc_found:
        acc_num = input("Please Enter the account number: ")
        for user in userList:
            if user.account_no == acc_num:
                acc_found = True
                print(f"Hello {user.first_name} {user.last_name}\n"
                      f"Balance: {user.balance}")
                transfer_amount = not_blank("Please Enter How Much You would like to transfer: ",
                                            "Please Enter a Valid Amount: ", False)
                transfer_amount = float(transfer_amount)
                while not acc_receive:
                    acc_send = input("What account would you like to send the money to:")
                    for recipient in userList:
                        if recipient.account_no == acc_send:
                            acc_receive = True
                            user.change_balance(user.balance - transfer_amount)
                            recipient.change_balance(recipient.balance + transfer_amount)
                            print(f"New Balance: {user.balance}\n"
                                  f"You have sent {transfer_amount} to {recipient.first_name} {recipient.last_name}")
                    if not acc_receive:
                        print("Sorry there was no account with that number.")
        if not acc_found:
            print("Sorry Please enter another number.")


def not_blank(question, error_message, let_ok):
    valid = False
    error = error_message
    while not valid:
        letter = False
        response = input(question)
        if not let_ok:
            for letter in response:
                if letter.isalpha():
                    letter = True

        if not response or letter is True:  # Generate Error for bad name
            print(error)
        else:
            return response


userList = []
generateUsers()

userChoice = ""
print("Welcome")

while userChoice != "Q":
    print("What function would you like to run?")
    print("Type 1 to find a user")
    print("Type 2 to print overdraft information")
    print("Type 3 to print users with missing emails")
    print("Type 4 to print bank details")
    print("Type 5 to transfer money")
    print("Type Q to quit")
    userChoice = input("Enter choice: ")
    print()

    if userChoice == "1":
        findUser()
    elif userChoice == "2":
        overdrafts()
    elif userChoice == "3":
        missingEmails()
    elif userChoice == "4":
        bankDetails()
    elif userChoice == "5":
        transfer()
    print()

import random
import csv
import os


class Account:
    def __init__(self):
        self.userid = random.randint(100, 900)
        self.type = None
        self.username = None
        self.password = None

    def addAdmin(self):
        self.type = "Admin"
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")

        with open('database.csv', 'a', newline='', encoding='utf-8') as database:
            writer = csv.writer(database)
            writer.writerow([self.userid, self.type, self.username, self.password])

        print(f"The user id generated is {self.userid}")

    def addCustomer(self):
        self.type = "Customer"
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")

        with open('database.csv', 'a', newline='', encoding='utf-8') as database:
            writer = csv.writer(database)
            writer.writerow([self.userid, self.type, self.username, self.password])

        print(f"The user id generated is {self.userid}")

    def deleteUser(self):
        userid = input("Enter user id to delete: ")

        temp_file = 'temp_database.csv'
        rows_kept = 0

        with open('database.csv', 'r', newline='',encoding='utf-8') as database, \
                open(temp_file, 'w', newline='',encoding='utf-8') as temp_db:

            reader = csv.reader(database)
            writer = csv.writer(temp_db)

            for row in reader:
                if row and row[0] != userid:
                    writer.writerow(row)
                    rows_kept += 1


        os.remove('database.csv')
        os.rename(temp_file, 'database.csv')

        if rows_kept < len(list(csv.reader(open('database.csv')))):
            print(f"User with ID {userid} has been deleted successfully.")
        else:
            print(f"No user found with ID {userid}.")

    def displayAccounts(self):
        try:
            with open('database.csv', 'r', newline='',encoding='utf-8') as accounts:
                reader = csv.reader(accounts)
                print("\nList of Accounts:")
                print("----------------")
                for row in reader:
                    if row:  # Skip empty rows
                        print(f"User ID: {row[0]}")
                        print(f"Type: {row[1]}")
                        print(f"Username: {row[2]}")
                        print(f"Password: {row[3]}")
                        print("----------------")
        except FileNotFoundError:
            print("No accounts found in the database. Please add accounts first.")
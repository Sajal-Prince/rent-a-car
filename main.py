import csv
from accounts import Account
from cars import Cars


def login():
    while True:
        username = input("Enter username (or 'q' to quit): ")
        if username.lower() == 'q':
            return None

        password = input("Enter password: ")

        try:
            with open('database.csv', 'r' , encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[2] == username and row[3] == password:
                        return row[1]
        except FileNotFoundError:
            pass

        print("Invalid username or password. Try again or press 'q' to quit.")


def main():
    account = Account()
    cars = Cars()

    while True:
        print("\n=== Car Rental System ===")
        print("1. Login")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user_type = login()

            while user_type:
                if user_type == "Admin":
                    print("\n=== ADMIN MENU ===")
                    print("1. Add User")
                    print("2. Remove User")
                    print("3. Display Users")
                    print("4. Add Car")
                    print("5. Remove Car")
                    print("6. Display Cars")
                    print("7. Logout")

                    admin_choice = input("Enter choice: ")

                    if admin_choice == "1":
                        user_type_input = input("Add Admin (a) or Customer (c)? ")
                        if user_type_input == "a":
                            account.addAdmin()
                        elif user_type_input == "c":
                            account.addCustomer()

                    elif admin_choice == "2":
                        account.deleteUser()

                    elif admin_choice == "3":
                        account.displayAccounts()

                    elif admin_choice == "4":
                        cars.addCar()

                    elif admin_choice == "5":
                        cars.deleteCar()

                    elif admin_choice == "6":
                        cars.displayCars()

                    elif admin_choice == "7":
                        break

                    else:
                        print("Invalid choice. Try again.")

                elif user_type == "Customer":
                    print("\n=== CUSTOMER MENU ===")
                    print("1. View Available Cars")
                    print("2. Logout")

                    customer_choice = input("Enter choice: ")

                    if customer_choice == "1":
                        cars.displayCars()

                    elif customer_choice == "2":
                        break

                    else:
                        print("Invalid choice. Try again.")

        elif choice == "2":
            print("Thank you for using Car Rental System!")
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")



main()
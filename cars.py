import csv
import random
import os


class Cars:
    def __init__(self):
        self.carId = random.randint(1111, 9999)
        self.carModel = None
        self.carManufacturer = None
        self.hourlyRate = None
        self.fuelType = None

    def addCar(self):
        self.carModel = input("Enter car Model : ")
        self.carManufacturer = input("Enter car Manufacturer : ")
        self.hourlyRate = input("Enter hourly Rate : ")
        self.fuelType = input("Enter fuel Type : ")

        with open('cars.csv', 'a', newline='', encoding='utf-8') as cars:
            writer = csv.writer(cars)
            writer.writerow([self.carId, self.carModel, self.carManufacturer, self.hourlyRate, self.fuelType])

        print(f"Car is added successfully... The car id generated is {self.carId}")

    def deleteCar(self):
        car_id = input("Enter car ID to delete: ")
        temp_file = 'temp_cars.csv'
        deleted = False

        with open('cars.csv', 'r', newline='', encoding='utf-8') as infile, open(temp_file, 'w', newline='', encoding='utf-8') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            for row in reader:
                if row and row[0] != car_id:
                    writer.writerow(row)
                else:
                    deleted = True

        os.remove('cars.csv')
        os.rename(temp_file, 'cars.csv')

        if deleted:
            print(f"Car with ID {car_id} deleted successfully")
        else:
            print(f"No car found with ID {car_id}")

    def displayCars(self):
        try:
            with open('cars.csv', 'r', newline='',encoding='utf-8') as cars:
                reader = csv.reader(cars)
                print("\nList of Cars:")
                print("-------------")
                for row in reader:
                    if row:  # Skip empty rows
                        print(f"ID: {row[0]}")
                        print(f"Model: {row[1]}")
                        print(f"Manufacturer: {row[2]}")
                        print(f"Hourly Rate: ${row[3]}/hour")
                        print(f"Fuel Type: {row[4]}")
                        print("-------------")
        except FileNotFoundError:
            print("No cars found in the database. Please add cars first.")
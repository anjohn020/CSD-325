##Changes Made:
## Added a user menu to select High Temperatures, Low Temperatures, or Exit.
## Extended the program to read and store low temperature data.
## Added a looping structure so the program continues running until the user chooses to exit.
## Implemented basic input validation to handle invalid user selections.


import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'

#Read this data once
dates, highs, lows = [], [], []

try:
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            try:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                dates.append(current_date)

                highs.append(int(row[5]))
                lows.append(int(row[6]))

#Skip rows with bad data to avoid crashes
            except ValueError:

                continue

#Added an error for file not found
except FileNotFoundError:
    print("Weather data file not found.")
    exit()

#Menu loop
while True:
    print("\nMenu Options:")
    print("Highs - View high temperatures")
    print("Lows - View low temperatures")
    print("Exit - Quit program")

    choice = input("Select option: ").strip().lower()

#Create graph for high temperatures
    if choice == "highs":
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
        plt.title("Daily high temperatures - 2018")
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)")
        plt.show()

#Create graph for low temperatures
    elif choice == "lows":
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')
        plt.title("Daily low temperatures - 2018")
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)")
        plt.show()

#Exit the program with a display message
    elif choice == "exit":
        print("Exiting program. Thank you for your support!")
        break

#Handles input error
    else:
        print("Invalid selection. Please type Highs, Lows, or Exit")
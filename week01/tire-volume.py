# For exceeding requirements, I asked customers for their phone number if they wanted to buy tires with the dimensions they added and put their phone number in the volumes text file

import math
import datetime

tire_width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = ((math.pi*(tire_width**2)*aspect_ratio)*((tire_width*aspect_ratio)+(2540*diameter)))/10000000000
volume = round(volume, 2)

print(f"The approximate volume is ", volume, "liters")

buy_question = input("Do you want to buy tires with the dimensions you entered? (yes or no): ").lower()

phone = 'no phone'
if buy_question == 'yes':
    phone = input("What is your phone number?: ")

current_date_and_time = datetime.datetime.now()

with open("volumes.txt", "at") as volumes_file:
    print(f"{current_date_and_time:%Y-%m-%d}", tire_width, aspect_ratio, diameter, volume, phone, file=volumes_file)

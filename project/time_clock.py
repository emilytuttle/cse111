import csv
from datetime import datetime



# Count the number of clock ins and outs
def check_in_or_out(filename):
    punch_count = 0
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row != '':
                punch_count += 1

    return punch_count


# Create a time punch:
def time_punch(filename, punch_type):
    # Get current date and create a list of pieces
    current_date_and_time = datetime.now()
    punch_data = [punch_type ,current_date_and_time.year, current_date_and_time.strftime("%b"), current_date_and_time.day, current_date_and_time.strftime("%H:%M")]
    # Create time punch
    with open(filename, 'a') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
    
        # writing the date and time, punch type, and pair
        csvwriter.writerow(punch_data)
        return 
    
# Get time clock data from file it in a user friendly format so they can see their punches
def view_punches(filename):
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        full_array = []
        print(f"\n")
        for row in reader:
            type_of_punch = row[0]
            day = row[3]
            month = row[2]
            year = row[1]
            time = row[4]
            print(day, month, year, ":", type_of_punch, time)
            new_list = time
            full_array.append(new_list)
  
    return full_array

def view_total_time(full_array):
    times_array = []
    pair_count = 0
    while len(full_array) > 0:
        pair_array = []
        while pair_count < 2:
            pair_array.append(full_array[0])
            full_array.pop(0)
            pair_count += 1
        pair_count = 0
        times_array.append(pair_array)
        pair_array = [] 
    hours_total = 0
    minutes_total = 0
    for i in times_array:
        if len(i) > 1:
            clockin_hour = i[0][0:2]
            clockout_hour = i[1][0:2]
            clockin_minute = i[0][3:5]
            clockout_minute = i[1][3:5]
            hour_difference = int(clockout_hour) - int(clockin_hour)
            minute_difference = int(clockout_minute) - int(clockin_minute)
            if minute_difference >= 60:
                while minute_difference >=60:
                    minute_difference - 60
                    hour_difference += 1
            hours_total += hour_difference
            minutes_total += minute_difference

    return [hours_total, minutes_total]
    


def main():
    file = "times.csv"
    clock_action = ""
    
    # Check if the count of current clock ins and outs is even or odd to determine if the next one will be in or out
    while clock_action != 0:
        check_in = int(check_in_or_out(file))
        if (check_in % 2) == 0: 
            is_in = "Clocked In!"
            punch_type = 'Punch IN'
        else:
            is_in = "Clocked Out!"
            punch_type = 'Punch OUT'
        print(check_in)
        print(f"\n")
        clock_action = int(input("Create a time punch (1)\nView your week's time clock(2) \nEnter a number: "))
        if clock_action == 1:
            print(f"\n")
            time_punch(file, punch_type)
            print("Time punch recorded.", is_in)
        if clock_action == 2:
            timeclock = view_punches(file)
            full_time = view_total_time(timeclock)
            print(timeclock)
            print("Total Time: ", full_time[0], "hours", full_time[1], "minutes")
        print(f"\n")
        clock_action= int(input("Do you want to do something else? Yes (1) or No (0): "))
    print("Thank you!")


if __name__ == "__main__":
    main()

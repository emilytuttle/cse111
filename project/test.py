from datetime import datetime
current_date_and_time = datetime.now()
time = current_date_and_time.strftime("%H:%M")
print(time)
print(time[0:2])
print(time[3:5])



 # times_array = []
    # pair_count = 0
    # while len(full_array) > 0:
    #     print("full array length: ", len(full_array))
    #     while pair_count < 2:
    #         pair_array = []
    #         pair_array.append(full_array[0])
    #         full_array.pop(0)
    #         pair_count += 1
    #         print("pair array: ", pair_array, "full array in pair while: ", full_array, len(full_array))
    #     pair_count = 0
    #     times_array.append(pair_array)
    # print(f"Full array: ", times_array)


    # for row in reader:
    #         if row != '':
    #             type_of_punch = row[0]
    #             day = row[3]
    #             month = row[2]
    #             year = row[1]
    #             time = row[4]
    #             print(day, month, year, ":", type_of_punch, time)
    #             new_list = [int(time[0:2]), int(time[3:5])]
            
    #             full_array.append(new_list)
# Exceeding requirements: I added a discount change. On Tuesdays and Wednesdays, the discount is 10% off the subtotal.


import csv
from datetime import datetime

current_date_and_time = datetime.now()
current_date_and_time = datetime.now()
print(f"{current_date_and_time:%A %I:%M %p}")

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    try:
        with open(filename, "rt") as csv_file:

            reader = csv.reader(csv_file)

            next(reader)

            for row_list in reader:
                key = row_list[key_column_index]

                dictionary[key] = row_list
    except KeyError as error:
        print('Error: Unknown product ID in the request.csv file', error)
    except FileNotFoundError as error:
        print('File not found')
        print(error)
    finally:
        print("Mission Accomplished")
    return dictionary

key_column_index = 0
dictionary = read_dictionary('products.csv', key_column_index)


def read_request(filename):
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        request = []
        for row_list in reader:
            item_and_quantity = []
            item = row_list[0]
            quantity = 0
            quantity += int(row_list[1])
            item_and_quantity.append(item)
            item_and_quantity.append(quantity)
            request.append(item_and_quantity)
    return(request)




def main():
   
    
    request = read_request('request.csv')

    print("All Products:")
    print(dictionary)
    print()
    print("Requested Items:")

    subtotal = 0
    sales_tax = 0

    # RECEIPT
    print("______________________________________")
    print("Smith's Marketplace")
    print()
    number_of_items = 0
    sales_tax_percent = 0.06
    discount = 0
    if f"{current_date_and_time:%A}" == "Wednesday" or "Tuesday":
        discount = 0.1
    for items in request:
        product = dictionary[items[0]]
        print(product[1], f': ', items[1], f'@ ', product[2] )
        subtotal += (float(product[2])* float(items[1]))
        number_of_items += int(items[1])
    
    sales_tax = subtotal * sales_tax_percent
    
    total = sales_tax + subtotal - (discount*subtotal)

    print()
    print(f"Number of Items:", number_of_items)
    print(f"Subtotal: ", round(subtotal, 2))
    if discount != 0:
            subtotal = subtotal - (subtotal*discount)
            print(f"Discount: ", round((subtotal*discount), 2))
    print(f"Sales tax: ", round(sales_tax, 2))
    print(f"Total: ", round(total, 2))
    print()
    print("Thank you for shopping at Smith's Marketplace!")
    print()
    print(f"{current_date_and_time:%A %I:%M %p}")
    print("______________________________________")

    





if __name__ == "__main__":
    main()

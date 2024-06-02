import csv

def read_dictionary(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    compound_list = []

    with open(filename, mode='rt') as csv_file:
        reader = csv.reader(csv_file)
        next(csv_file)
        for row_list in reader:
            if len(row_list) != 0:
                compound_list.append(row_list)

        return compound_list

    



def main():
    compound_list = read_dictionary('students.csv')
    dictionary = dict(compound_list)

    i_number = input("What is the I-Number? (xxxxxxxxx): " )

    if i_number in dictionary:
        print(dictionary[i_number])
    else: print('No such student')



if __name__ == "__main__":
    main()
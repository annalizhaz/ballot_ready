import csv
import numpy as np
import string
import sys

def read_csv(filename):

    '''
    Read in csv file (filename) and create array from it.

    Returns numpy array
    '''
    with open(filename, "r") as f:
        reader = csv.reader(f)
        data_in_lists = list(reader)

    empty_rows_removed = []

    for i, row in enumerate(data_in_lists):
        if len(row) != 0:
            empty_rows_removed.append(row)

    data_array = np.array(empty_rows_removed[1:]) #removes header row
    return data_array

def column_to_number(alpha_column):
    '''
    Takes column labels as they are in excel(i.e., "A", "AB", etc.) an translates 
    them to the corresponding number
    '''

    #add exception for incorrect value types given for columns

    column_label = list(alpha_column)

    num = 0

    for letter in alpha_column:
        if letter in string.ascii_letters:
            num = num * 26 + (ord(letter.upper()) - ord("A")) + 1

    return num

def fetch_data(data_array, data_dict, first_name_number, last_name_number, data_number_start, data_number_end):

    '''
    Takes numpy array, empty dictionary, and parameters for which columns contain
    labels and which columns contain data to be retrieved and condensed.

    Returns dictionary with lavels as keys and data as values in a list
    '''

    first_names = list(data_array[:, (first_name_number - 1)])
    last_names = list(data_array[:, (last_name_number - 1)])
    urls = data_array[:, (data_number_start - 1):(data_number_end)]

    #candidates must all have unique last names for this to work

    for i, last_name in enumerate(last_names):
        name_key = last_name
        if name_key not in data_dict:
            data_dict[name_key] = {"first name" : first_names[i], "last name" : last_names[i], "issue urls" : set(urls[:, i])}
        else:
            data_dict[name_key]["issue urls"].update(set(urls[:, i]))


def write_new(data_dict, write_to):
    '''
    Takes filled in dictionary and filepath for new file

    Writes csv to new file location with data from dictionary in the format:

    last name , first name, url
    last name, first name, url

    One url per row
    Names repeat for as many urls as they are associated with
    
    '''
    with open(write_to, 'w') as csvfile:
        mywriter = csv.writer(csvfile, dialect='excel')

        for key in data_dict:
            for url in data_dict[key]["issue urls"]:
                if url != "{}":
                    mywriter.writerow([data_dict[key]["last name"], data_dict[key]["first name"], url])


def go(filename, first_name_column, last_name_column, data_column_start, data_column_end, write_to):
    '''

    '''
    data_dict = {}

    data_array = read_csv(filename)

    first_name_number = column_to_number(first_name_column)
    last_name_number = column_to_number(last_name_column)
    data_number_start = column_to_number(data_column_start)
    data_number_end = column_to_number(data_column_end)

    fetch_data(data_array, data_dict, first_name_number, last_name_number, data_number_start, data_number_end)

    write_new(data_dict, write_to)

if __name__ == "__main__":
    usage = "python3 mechanical_turk_processor.py <'read from file'> <'first name column'>\
    <'last name column'> <'data start column'> <'data end column'> <'new file path'>"
    args_len = len(sys.argv)
    if args_len != 7:
        raise ValueError("Incorrect number of arguments provided")
        print(usage)
        sys.exit(0)
    else:

        filename = sys.argv[1]
        first_name_column = sys.argv[2]
        last_name_column = sys.argv[3]
        data_column_start = sys.argv[4]
        data_column_end = sys.argv[5]
        write_to = sys.argv[6]

        go(filename, first_name_column, last_name_column, data_column_start, data_column_end, write_to)

        print(usage)    
        sys.exit(0)
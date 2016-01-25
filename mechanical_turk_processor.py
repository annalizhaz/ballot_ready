import csv
import numpy as np
import string

def read_csv(filename):

'''
Read in csv file (filename) and create array from it.

Returns numpy array
'''
    with open(filename, "r") as f:
        reader = csv.reader(f)
        data_in_lists = list(reader)

    for i, row in enumerate(data_in_lists):
        if len(row) == 0:
            data_in_lists.pop(i)

    data_array = np.array(data_in_lists)
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
            num = num * 26 + (ord(letter.upper()) - order("A"))
            #not adding 1 to above because indexing starts at 0

    return num

def fetch_data(data_array, data_dict, first_name_number, last_name_number, data_number_start, data_number_end):

'''
Takes numpy array, empty dictionary, and parameters for which columns contain
labels and which columns contain data to be retrieved and condensed.

Returns dictionary with lavels as keys and data as values in a list
'''

    first_names = list(data_array[:, first_name_number])
    last_names = list(data_array[:, last_name_number])
    urls = data_array[:, data_number_start:(data_number_end+1)]

    #candidates must all have unique last names for this to work

    for i, last_name in last_names:
        name_key = last_name
        if name_key not in data_dict:
            data_dict[name_key] = {"first name" : first_names[i], "last name" : last_names[i], "issue urls" : set(urls[:, i])}
        else:
            data_dict[name_key]["issue urls"].update(set(urls[:, i]))

    


def go(filename, first_name_column, last_name_column, data_column_start, data_column_end, write_to):
    '''

    '''
    data_dict = {}

    data_array = read_csv(filename)

    first_name_number = column_to_number(first_name_column)
    last_name_number = column_to_number(last_name_number)
    data_number_start = column_to_number(data_column_start)
    data_number_end = column_to_number(data_column_end)

    fetch_data(data_array, data_dict, first_name_number, last_name_number, data_number_start, data_number_end)

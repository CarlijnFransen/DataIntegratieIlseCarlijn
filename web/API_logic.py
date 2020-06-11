"""
Author: Ilse den Brok
Date: 11 June 2020
Function: makes a structured list from a file given by the user
"""
import csv


def main():
    input_attribute = read_input_file()
    input_list = structure_list(input_attribute)


def read_input_file():
    """
    the input file is split into its header and attributes
    :return: input_attribute is a list with information from the user
    """
    input_file = "../input_file.txt"
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        input_attribute = []
        header = []
        row_counter = 0
        for row in reader:
            if row_counter == 0:
                header.append(row)
            else:
                input_attribute.append(row)
            row_counter += 1
    return input_attribute


def structure_list(input_attribute):
    """
    makes a structured list with attributes in the form
    'chromosome_position_reference nucleotide_alternative nucleotide'
    :param input_attribute:
    :return: input_list is the structured list with all complete instances
    """
    input_list = []
    for line in input_attribute:
        if len(line) == 4:
            regel = line[0] + '_' + line[1] + '_' + line[2] + '_' + line[3]
            input_list.append(regel)
            print(regel)
        else:
            print('One or more of your entries did not contain all 4 elements, these will be ignored')
    return input_list


main()

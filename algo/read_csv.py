"""
Reads the second column of every odd row of the CSV file.
"""
import csv


def read_2_col_odd_rows(file_name):
    """Reads the csv file according to the module description"""
    return [row[1] for i, row
            in enumerate(csv.reader(open(file_name, newline='')))
            if i % 2]

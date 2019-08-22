"""
Reads the second column of every odd row of the CSV file.
"""
import csv

def read_2_col_odd_rows(file_name):
    with open(file_name, newline='') as csv_input:
        return [row[1] for i, row in enumerate(csv.reader(csv_input)) if i % 2]

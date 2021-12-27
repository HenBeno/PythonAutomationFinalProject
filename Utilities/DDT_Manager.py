import csv

import allure


@allure.step("reading data from csv")
def read_data_from_csv(filename):
    # create empty list
    data_list = []
    # open csv file
    csv_data = open(filename, "r")

    # create csv reader
    reader = csv.reader(csv_data)
    # skip header
    next(reader)
    # add csv rows to list
    for rows in reader:
        data_list.append(rows)
    return data_list

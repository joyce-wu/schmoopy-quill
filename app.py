import numpy as np
import pandas as pd

def csv_to_array(file):
    f = open(file, 'r')
    data = f.read()
    lines = data.split("\n")
    ret = []
    for line in lines:
        array = line.split(",")
        ret.append(array)
    return ret

def create_time_table(file):
    row = 25
    column = 10
    new_row = []
    table = [[0 for x in range(column)] for y in range(row)]
    data = csv_to_array(file)
    for i in range(row):
        for y in range(column):
            table[i][y] = data[i][y]
    for i in range(9, 32):
        for y in range(column):
            new_row.append(table[i][y]+str(8*60))
        table.append(new_row)
        new_row = []
    print(table)


create_time_table('sat_timetable_s.csv')


stops = {
    "142": "South Ferry",
    "137": "Chambers Street",
    "127": "42 Street Times Square",
    "125": "59 Street Columbus Circle",
    "120": "96 Street",
    "115": "137 Street",
    "112": "168 Street",
    "104": "231 Street",
    "103": "238 Street",
    "101": "242 Street"
}

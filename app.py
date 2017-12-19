import numpy as np
import pandas as pd

def csv_to_array(file):
    i=0
    new = []
    ret = []
    f = open(file, 'r')
    data = f.read()
    sections = data.split("\n\n")
    counter = len(sections)
    while i < counter:
        lines = sections[i].split("\n")
        for line in lines:
            array = line.split(",")
            new.append(array)
        ret.append(new)
        new = []
        i+=1
    return ret

def create_time_table_sat(file):
    data = csv_to_array(file)
    group = len(data)
    row = len(data[0])
    column = 10
    new_row = []
    z = 0
    x = 0
    prev_row = 0
    table = [[0 for x in range(column)] for y in range(row)]
    while z < group:
        section = data[z]
        row = len(data[z])
        if z == 0:
            for i in range(row):
                for y in range(column):
                    table[i][y] = section[i][y]
        else:
            for i in range(prev_row-1 , prev_row + row):
                for y in range(column):
                    table[i][y] = section[i][y]
        if x < 3:
            end =  int((int(data[z+1][0][0])- int(section[len(section) -1][0]))/(60*8))
            for i in range(row-1, end):
                for y in range(column):
                    new_row.append(table[i][y]+str(8*60))
                table.append(new_row)
                new_row = []
            prev_row = prev_row + i
            print(len(table[0]))
            print(len(table))
        z+=1
        x+=1
    print(table)

create_time_table_sat('sat_timetable_n.csv')

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

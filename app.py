import numpy as np
import pandas as pd
import copy
import csv
import random

stops = { #corresponding column to stop
    "142": 0,
    "137": 1,
    "127": 2,
    "125": 3,
    "120": 4,
    "115": 5,
    "112": 6,
    "104": 7,
    "103": 8,
    "101": 9
}

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

def create_actual_table(actual, day):
    f = open(actual, 'r')
    data = f.read()
    lines = data.split("\n")
    ret = []
    for line in lines:
        if(line == ""):
            pass
        else:
            stop = line.split(",")[1]
            time = line.split(",")[2]
            closest_time = find_closest_time(stop, time, day)
            #print(closest_time)
            if(closest_time != None):
                print("closest: " + str(closest_time) + "time: " + time)
                time_difference = int(time) - closest_time
                #print(time_difference)
                ret.append([int(stop[0:3]), time_difference])
    return ret

def find_closest_time(stop, time, day):
    direction = stop[-1]
    time = int(time)
    if(day == "monday" or day == "tuesday"):
        file_name = "weekday/scheduled/weekday_" + direction + ".csv"
    elif(day == "saturday"):
        file_name = "saturday/scheduled/sat_" + direction + ".csv"
    scheduled_array = csv_to_array(file_name)
    #print(scheduled_array)
    try:
        stop = stops[stop[0:3]]
        #print(stop)
        smallest_diff = time - int(scheduled_array[0][0][int(stop)])
        smallest_time = int(scheduled_array[0][0][int(stop)])
        #print(smallest_time)
        for row in range(len(scheduled_array)):
            if time - int(scheduled_array[0][row][stop]) < smallest_diff:
                print(smallest_diff)
                smallest_time = int(scheduled_array[0][row][stop])
        return smallest_time
    except:
        return

def unix_to_min(array):
    for i in range(len(array)):
        array[i][1] = 60 - array[i][1]/3600
    return array


ret = create_actual_table("weekday/monday/actual/monday.csv", "monday")
print(ret)
la = unix_to_min(ret)
print(ret)




def create_time_table_sat(file):
    data = csv_to_array(file)
    group = len(data)
    #numer of rows of first group
    row = len(data[0])
    column = 10
    new_row = []
    current_group = 0
    gaps = 0
    prev_row = 0
    table = [[0 for x in range(column)] for y in range(row)]
    while current_group < group:
        a = 0
        section = data[current_group]
        if current_group == 3:
            section = section[0:-1]
        row = len(section)
        if current_group == 0:
            for i in range(row):
                for y in range(column):
                    table[i][y] = section[i][y]
        else:
            while a < row:
                for y in range(column):
                    new_row.append(section[a][y])
                a+=1
                if(current_group == 2):
                    print(str(a) + str(new_row))
                r = copy.deepcopy(new_row)
                print(r)
                table.append(r)
                new_row = []
        if gaps < 3:
            end =  int((int(data[current_group+1][0][0])- int(section[len(section) -1][0]))/(60*8))
            for i in range(row-1, end):
                for y in range(column):
                    new_row.append(str((int(table[i][y])+8*60)))
                table.append(new_row)
                new_row = []
            prev_row = prev_row + i
        if(current_group == 2 or current_group == 3):
            print("================table============")
            print(table)
        current_group+=1
        gaps+=1
    print("===========3rd section==============")
    print(data[2])
    return table

def array_to_csv(array, file):
    f = open(file, 'w+')
    for row in range(len(array)):
        for column in range(len(array[0])):
            f.write(array[row][column]+',')
        f.write("\n")
    f.close()

stop_ids = ['142', '137', '127', '125', '120', '115', '112', '104', '103', '101']
def generate_times(stop_list, file):
    i = 0
    while i < 40:
        print random.uniform(0.0, 8.0)
        i += 1

generate_times(stop_ids, 'time_dif.csv')



#array_to_csv(create_time_table_sat('saturday/scheduled/sat_timetable_s.csv'), 'sat_s.csv')

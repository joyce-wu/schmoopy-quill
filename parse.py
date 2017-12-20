import json
from pprint import pprint

def parse_real_time_data(file, output):
    data = json.load(open(file))
    #data['entity'] contains all the train time information
    d = data['entity']
    heading = "line,stop_id,arrival time"
    #parsing through the entities
    #increment by 2 because the odd ones don't have time data
    for i in range(0, len(d)):
        with open(output,'a') as f:
            #attempting to only grab 1 train data
            line = "" #next line of the csv file
            label = "1" #train line that we want
            try:
                train_line = d[i]['trip_update']['trip']['route_id']
                if train_line == label:
                    print("\n========================================================")
                    ent = d[i]['trip_update']['stop_time_update']
                    for x in range(0, len(ent)):
                        #train_line
                        line = label + ","
                        #stop_id
                        print("\nstop id: " + str(ent[x]['stop_id']))
                        line = line + str(ent[x]['stop_id'])+","
                        #arrival_time
                        print("unix arrival time: " + str(ent[x]['arrival']['time']))
                        line = line + str(ent[x]['arrival']['time'])
                        #print("\n" + str(d[i]['trip_update']['stop_time_update'][0]['arrival']['time']) + ",")
                        print(line)
                        f.write(line+"\n")
            except:
                pass
        f.close()

def parse_timetable(file):
    d = open(file, 'r')
    data = d.read()
    base_time = 1513400400 #add to every time to convert to unix from 12/16/2017
    #train stops for 1 train
    heading = "South Ferry, Chambers St, 42 st, 59 st, 96 st, 137 st, 168 st, 231 st, 238 st, 242 st"
    with open('sat_timetable_s.csv', 'a') as f:
        lines = data.split("\n")
        lines = lines[0:-1]
        for line in lines: #removes last empty newline
            add_line = "" #line to be added to csv
            times = line.split(" ") #creates list of times per line
            for time in times:
                unix_time = base_time
                hour = int(time.split(":")[0]) #retrieves hour and minute
                minute = int(time.split(":")[1][0:2])
                unix_time += hour*3600 + minute*60 #conversion to unix time
                add_line += str(unix_time) + ","
            add_line = add_line[0:-1] #removes last comma
            print(add_line)
            f.write(add_line+"\n")
    f.close()

def missing_times(start, end, interval):
    start_hour = int(start.split(":")[0])
    start_min = int(start.split(":")[1])
    start_total = start_hour * 60 + start_min
    end_hour = int(end.split(":")[0])
    end_min = int(end.split(":")[1])
    end_total = end_hour * 60 + end_min
    times = []
    cont = True
    print("start " + str(start_total) + " end " + str(end_total))
    while(cont):
        if start_total + 3 > end_total:
            print("ha")
            cont = False
            break
        else:
            start_total += interval
            times.append(start_total)
    for i in range(0, len(times)):
        time = times[i]
        hour = time / 60
        minute = time % 60
        if minute < 10:
            minute = ":0" + str(minute)
        if hour > 12:
            hour = hour%12
        print(str(hour) + ":" + str(minute))

# print("===================  south ferry ================")
# missing_times("6:40", "10:56", 8)
# print("===================12:005==============")
# missing_times("12:00", "14:00", 8)
# print("===================4:07================")
# missing_times("3:04", "8:08", 8)
# print("=================== chambers ===================")
# missing_times("6:41", "10:57", 8)
# print("===================12:04================")
# missing_times("12:01", "14:01", 8)
# print("===================4:12================")
# missing_times("3:05", "8:09", 8)
# print("===================42 st================")
# missing_times("6:53", "11:09", 8)
# print("===================12:17================")
# missing_times("12:13", "14:13", 8)
# print("===================4:25================")
# missing_times("3:17", "8:21", 8)
# print("===================59 st================")
# missing_times("6:58", "11:14", 8)
# print("===================12:21================")
# missing_times("12:18", "14:18", 8)
# print("===================4:29================")
# missing_times("3:22", "8:26", 8)
# print("===================96 st================")
# missing_times("7:04", "11:20", 8)
# print("===================12:28================")
# missing_times("12:24", "14:24", 8)
# print("===================4:36================")
# missing_times("3:28", "8:32", 8)
# print("===================137 st================")
# missing_times("7:06", "11:22", 8)
# print("===================12:37================")
# missing_times("12:26", "14:26", 8)
# print("===================4:45================")
# missing_times("3:30", "8:34", 8)
# print("===================168 st================")
# missing_times("7:12", "11:28", 8)
# print("===================12:42================")
# missing_times("12:32", "14:32", 8)
# print("===================4:50================")
# missing_times("3:36", "8:40", 8)
# print("===================231================")
# missing_times("7:17", "11:33", 8)
# print("===================12:52================")
# missing_times("12:37", "14:37", 8)
# print("===================5:00================")
# missing_times("3:41", "8:45", 8)
# print("===================238================")
# missing_times("7:32", "11:48", 8)
# print("===================12:56================")
# missing_times("12:52", "14:52", 8)
# print("===================5:04================")
# missing_times("3:56", "9:00", 8)
# print("===================242================")
# missing_times("7:37", "11:53", 8)
# print("===================12:58================")
# missing_times("12:57", "14:57", 8)
# print("===================5:06================")
# missing_times("4:01", "9:05", 8)
#parse_real_time_data('monday/actual/monday.json', 'monday/actual/monday.csv')
parse_timetable('saturday_timetable_south.txt')

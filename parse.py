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
    with open('weekday_timetable_n.csv', 'a') as f:
        lines = data.split("\n")
        lines = lines[0:-1]
        for line in lines: #removes last empty newline
            add_line = "" #line to be added to csv
            times = line.split(" ") #creates list of times per line
            for time in times:
                if(time.strip() == '\xe2\x80\x94'):
                    add_line += str(0) + ","
                else:
                    unix_time = base_time
                    hour = int(time.split(":")[0]) #retrieves hour and minute
                    minute = int(time.split(":")[1][0:2])
                    unix_time += hour*3600 + minute*60 #conversion to unix time
                    add_line += str(unix_time) + ","
            add_line = add_line[0:-1] #removes last comma
            #print(add_line)
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
            minute = "0" + str(minute)
        if hour > 12:
            hour = hour%12
        print(str(hour) + ":" + str(minute))

# print("===================  south ferry ================")
# missing_times("8:40", "11:58", 5)
# print("===================12:005==============")
# missing_times("12:40", "15:27", 6)
# print("===================4:07================")
# missing_times("3:56", "8:18", 4)
# print("=================== chambers ===================")
# missing_times("8:46", "12:02", 5)
# print("===================12:04================")
# missing_times("12:44", "15:32", 6)
# print("===================4:12================")
# missing_times("4:01", "8:23", 4)
# print("===================42 st================")
# missing_times("8:59", "12:15", 5)
# print("===================12:17================")
# missing_times("12:57", "15:44", 6)
# print("===================4:25================")
# missing_times("4:14", "8:36", 4)
# print("===================59 st================")
# missing_times("9:03", "12:19", 5)
# print("===================12:21================")
# missing_times("1:01", "3:48", 6)
# print("===================4:29================")
# missing_times("4:19", "8:40", 4)
# print("===================96 st================")
# missing_times("9:10", "12:26", 5)
# print("===================12:28================")
# missing_times("1:08", "3:56", 6)
# print("===================4:36================")
# missing_times("4:27", "8:47", 4)
# print("===================137 st================")
# missing_times("9:18", "12:35", 5)
# print("===================12:37================")
# missing_times("1:17", "4:04", 6)
# print("===================4:45================")
# missing_times("4:35", "8:55", 4)
# print("===================168 st================")
# missing_times("9:23", "12:40", 5)
# print("===================12:42================")
# missing_times("1:22", "4:09", 6)
# print("===================4:50================")
# missing_times("4:40", "9:00", 4)
# print("===================231================")
# missing_times("9:34", "12:50", 5)
# print("===================12:52================")
# missing_times("1:32", "4:20", 6)
# print("===================5:00================")
# missing_times("4:51", "9:11", 4)
# print("===================238================")
# missing_times("9:36", "12:54", 5)
# print("===================12:56================")
# missing_times("1:36", "4:22", 6)
# print("===================5:04================")
# missing_times("4:54", "9:12", 4)
# print("===================242================")
# missing_times("9:38", "12:56", 5)
# print("===================12:58================")
# missing_times("1:38", "4:23", 6)
# print("===================5:06================")
# missing_times("4:55", "9:14", 4)
#parse_real_time_data('monday/actual/monday.json', 'monday/actual/monday.csv')
parse_timetable('weekday_north.txt')

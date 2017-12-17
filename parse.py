import json
from pprint import pprint

def parse_real_time_data(file):
    data = json.load(open(file))
    #data['entity'] contains all the train time information
    d = data['entity']
    heading = "line,stop_id,arrival time"
    #parsing through the entities
    #increment by 2 because the odd ones don't have time data
    for i in range(0, len(d), 2):
        with open('output.csv','a') as f:
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
    with open('mon_timetable_s.csv', 'a') as f:
        lines = data.split("\n")
        lines = lines[0:-1]
        for line in lines: #removes last empty newline
            add_line = "" #line to be added to csv
            times = line.split(" ") #creates list of times per line
            for time in times:
                unix_time = base_time
                hour = int(time.split(":")[0]) #retrieves hour and minute
                minute = int(time.split(":")[1])
                unix_time += hour*3600 + minute*60 #conversion to unix time
                add_line += str(unix_time) + ","
            add_line = add_line[0:-1] #removes last comma
            print(add_line)
            f.write(add_line+"\n")
    f.close()

parse_real_time_data('formatted_output.json')
parse_timetable('saturday_timetable_north.txt')

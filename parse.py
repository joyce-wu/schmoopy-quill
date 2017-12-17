import json
from pprint import pprint

data = json.load(open('formatted_output.json'))

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

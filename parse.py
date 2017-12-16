import json
from pprint import pprint

data = json.load(open('formatted_output.json'))

#data['entity'] contains all the train time information
d = data['entity']

#parsing through the entities
#increment by 2 because the odd ones don't have time data
for i in range(0, len(d), 2):
    #attempting to only grab 1 train data
    label = ""
    try:
        label = d[i]['trip_update']['trip']['route_id']
    except:
        pass
    #change label to whatever train you want
    if label == "1":
        print("\n========================================================")
        #don't really know what train id is but yeah
        print("train id: " + str(d[i]['id']))
        print("========================================================")
        try:
            ent = d[i]['trip_update']['stop_time_update']
            for x in range(0, len(ent)):
                print("\nstop id: " + str(ent[x]['stop_id']))
                print("unix arrival time: " + str(ent[x]['arrival']['time']) + ",")
                #print("\n" + str(d[i]['trip_update']['stop_time_update'][0]['arrival']['time']) + ",")
        except:
            pass

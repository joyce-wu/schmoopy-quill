import json
from pprint import pprint

data = json.load(open('formatted_output.json'))

#pprint(data['entity'][50])
#pprint(data['entity'][2])
#pprint(data['entity'][3])
d = data['entity']
#pprint(str(d[0]['trip_update']['stop_time_update'][2]))

for i in range(0, len(d), 2):
    #print(label = d[i]['trip'])
    label = ""
    try:
        label = d[i]['trip_update']['trip']['route_id']
    except:
        pass
    if label == "1":
        print("\n========================================================")
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

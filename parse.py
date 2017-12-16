import json
from pprint import pprint

data = json.load(open('formatted_output.json'))

pprint(data['entity'][50])
#pprint(data['entity'][2])
#pprint(data['entity'][3])
d = data['entity']
for i in range(0, len(d), 2):
    print("==============I: " + str(i) + "================")
    try:
        print("\n" + str(d[i]['trip_update']['stop_time_update'][0]['arrival']['time']) + ",")
    except:
        

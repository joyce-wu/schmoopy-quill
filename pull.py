#import schedule
import time
import urllib
import os

key = "233db5c5454f7a125d8e129aff2503d1"
global count = 0

urls = {
    #1,2,3,4,5,6,S
    "1": "http://datamine.mta.info/mta_esi.php?key=" + key + "&feed_id=1",
    #A,C,E
    "26": " http://datamine.mta.info/mta_esi.php?key=" + key + "&feed_id=26",
    #N,Q,R,W
    "16": " http://datamine.mta.info/mta_esi.php?key=" + key + "&feed_id=16",
    #B,D,F,N
    "21": " http://datamine.mta.info/mta_esi.php?key=" + key + "&feed_id=21",
    #L
    "2": " http://datamine.mta.info/mta_esi.php?key=" + key + "&feed_id=2",
    #G
    "31": " http://datamine.mta.info/mta_esi.php?key=" + key + "&feed_id=31",
    #J,Z
    "36": " http://datamine.mta.info/mta_esi.php?key=" + key + "&feed_id=36",
    #7
    "51": " http://datamine.mta.info/mta_esi.php?key=" + key + "&feed_id=51"
}

def convert():
    os.system("gtfs_realtime_json/dist/gtfs_realtime_json " + urls["1"] > "output"+count+".json")
    count+=1

def main():
    convert()

if __name__ == '__main__':
    main()

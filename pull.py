import schedule
import time
import urllib
import os
import datetime
import json
from pymongo import MongoClient
from pprint import pprint

#export PYTHONPATH="${PYTHONPATH}/usr/local/lib/python2.7/site-packages:/usr/lib/python2.7/site-packages"
#using mongodb to handle adding json to database
#testing

client = MongoClient('lisa.stuy.edu', 27017)
db = client.time #database is called time
col = db.data
posts = db.posts
#inserting posts
#find w/ json files

key = "233db5c5454f7a125d8e129aff2503d1"
#default global date value
date = ""

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

#updates at 11:59 every night to respective .json file
def convert():
    #os.system("gtfs_realtime_json/dist/gtfs_realtime_json " +str(urls["1"])+ " > 1.json")
    os.system("./gtfs_realtime_json 'http://datamine.mta.info/mta_esi.php?key=233db5c5454f7a125d8e129aff2503d1&feed_id=1' > 1.json")
    os.system("./gtfs_realtime_json 'http://datamine.mta.info/mta_esi.php?key=233db5c5454f7a125d8e129aff2503d1&feed_id=26' > 26.json")
    os.system("./gtfs_realtime_json 'http://datamine.mta.info/mta_esi.php?key=233db5c5454f7a125d8e129aff2503d1&feed_id=16' > 16.json")
    os.system("./gtfs_realtime_json 'http://datamine.mta.info/mta_esi.php?key=233db5c5454f7a125d8e129aff2503d1&feed_id=21' > 21.json")
    os.system("./gtfs_realtime_json 'http://datamine.mta.info/mta_esi.php?key=233db5c5454f7a125d8e129aff2503d1&feed_id=2' > 2.json")
    os.system("./gtfs_realtime_json 'http://datamine.mta.info/mta_esi.php?key=233db5c5454f7a125d8e129aff2503d1&feed_id=31' > 31.json")
    os.system("./gtfs_realtime_json 'http://datamine.mta.info/mta_esi.php?key=233db5c5454f7a125d8e129aff2503d1&feed_id=36' > 36.json")
    os.system("./gtfs_realtime_json 'http://datamine.mta.info/mta_esi.php?key=233db5c5454f7a125d8e129aff2503d1&feed_id=51' > 51.json")

def fetch_date():
    now = datetime.datetime.now()
    global date
    date = str(now.month) + "-" + str(now.day) + "-" + str(now.year)
    print date

def add_db():


def main():
    global date
    schedule.every().day.at("23:59").do(convert)
    schedule.every().day.at("23:59").do(fetch_date)
    #schedule.every().day.at("20:33").do(add_db)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()

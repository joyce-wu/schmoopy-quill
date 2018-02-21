import schedule
import time
import urllib
import os
import subprocess
import sqlite3
import datetime
import json

#export PYTHONPATH="${PYTHONPATH}/usr/local/lib/python2.7/site-packages:/usr/lib/python2.7/site-packages"

key = "233db5c5454f7a125d8e129aff2503d1"
#deafult global date value
date = ""

db = sqlite3.connect('data.db')
c = db.cursor()
c.execute("CREATE TABLE IF NOT EXISTS data (mmddyyy TEXT, json BLOB)")
db.commit()
db.close()

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
    db = sqlite3.connect('data.db')
    c = db.cursor()
    with open('1.json') as json_data:
        d = json.load(json_data)
        json_data.close()
        c.execute("INSERT INTO data VALUES(?, ?)", (date,d))
    with open('26.json') as json_data:
        d = json.load(json_data)
        json_data.close()
        c.execute("INSERT INTO data VALUES(?, ?)", (date,d))
    with open('16.json') as json_data:
        d = json.load(json_data)
        json_data.close()
        c.execute("INSERT INTO data VALUES(?, ?)", (date,d))
    with open('21.json') as json_data:
        d = json.load(json_data)
        json_data.close()
        c.execute("INSERT INTO data VALUES(?, ?)", (date,d))
    with open('2.json') as json_data:
        d = json.load(json_data)
        json_data.close()
        c.execute("INSERT INTO data VALUES(?, ?)", (date,d))
    with open('31.json') as json_data:
        d = json.load(json_data)
        json_data.close()
        c.execute("INSERT INTO data VALUES(?, ?)", (date,d))
    with open('36.json') as json_data:
        d = json.load(json_data)
        json_data.close()
        c.execute("INSERT INTO data VALUES(?, ?)", (date,d))
    with open('51.json') as json_data:
        d = json.load(json_data)
        json_data.close()
        c.execute("INSERT INTO data VALUES(?, ?)", (date,d))
    db.commit()
    db.close()


def main():
    global date
    schedule.every().day.at("23:59").do(convert)
    #schedule.every().day.at("20:33").do(fetch_date)
    #schedule.every().day.at("20:33").do(add_db)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()

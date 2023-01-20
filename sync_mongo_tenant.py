import pymongo
import time

client_from = pymongo.MongoClient("127.0.0.1:27017")
client_to = pymongo.MongoClient("mongodb://hp_iibd:4hxCQsbSP4ryEXRMg8@103.19.110.150")

def func_col_from():
    return client_from.ewsdb.honeypots
def func_col_to():
    return client_to.hp_iibd_1.honeypots
def func_col_to_time():
    return client_to.hp_iibd_1.honeypotstime

col_from = func_col_from()
col_to_time = func_col_to_time()
print(col_from)
print(col_to_time)

for hp in col_from.distinct("tags.honeypot"):
    col_to_time.insert_one({"honeypot": hp, "time": "2022-01-01T00:00:00+0000"})

cnt = 0

while True:
    try:
        client_to.server_info()
        client_from.server_info()
        print("Connection is OK")
        
        col_from = func_col_from()
        col_to = func_col_to()
        col_to_time = func_col_to_time()
        
        distinct_hp = col_from.distinct("tags.honeypot")
        
        for hp in distinct_hp:
            
            col_from = func_col_from()
            col_to = func_col_to()
            col_to_time = func_col_to_time()
            
            print("Honeypot Type:", hp)
            last_hp = [x for x in col_to_time.find({"honeypot": hp}).sort("time", -1).limit(1)][0]['time']
            print("Last time:", last_hp)
            for x in col_from.find({"tags.honeypot": hp, "time": {"$gt": last_hp}}).sort("time", 1):
                while True:
                    try:
                        col_to.insert_one(x)
                        cnt += 1
                        break
                    except pymongo.errors.DuplicateKeyError as err:
                        print(err)
                        print("Duplicate document. Skipping...")
                        break
                    except:
                        print("Fail to insert to hp")
                        time.sleep(10)
                        col_to = func_col_to()
                while True:
                    try:
                        col_to_time.insert_one({"honeypot": hp, "time": x["time"]})
                        break
                    except:
                        print("Fail to insert to time")
                        time.sleep(10)
                        col_to_time = func_col_to_time()
                if cnt % 10000 == 0:
                    print("Jumlah data masuk: ", str(cnt))
        print("One loop done")
        time.sleep(60)
    except pymongo.errors.ServerSelectionTimeoutError as err:
        print(err)
        time.sleep(60)
    except:
        print("Other errors")
        time.sleep(60)

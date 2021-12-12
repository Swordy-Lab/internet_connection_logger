import rs_privat_module
import datetime
from time import sleep, time
import os

config = rs_privat_module.import_json("config.json")

if not os.path.exists("Logs"):
    os.makedirs("Logs")

last = 0
downtime = 0 

while(True):
    status = rs_privat_module.fastping(config["url"])
    
    if status:
        if last == 0:
            rs_privat_module.Log_to_file("Connected", 0, "Logs", (str(datetime.date.today()) + ".log"), True, True)
            last = 2
        elif last == 1:
            stop = time()
            downtime = stop - start
            rs_privat_module.Log_to_file(("Connection restored" + " | Downtime " + str(int(downtime))), 1, "Logs", (str(datetime.date.today()) + ".log"), True, True)
            last = 0
            

    else:
        if last == 0 or last == 2:
            if rs_privat_module.fastping("192.168.0.1"):
                start = time()
                rs_privat_module.Log_to_file("Connection lost", 2, "Logs", (str(datetime.date.today()) + ".log"), True, True)
                last = 1
            else:
                rs_privat_module.Log_to_file("Connection lost. No connection to gateway.", 1, "Logs", (str(datetime.date.today()) + ".log"), True, True)

    sleep(5)
import rs_privat_module
import datetime
from time import sleep, time
import os
config = rs_privat_module.import_json("config.json")


last = 0
downtime = 0

while(True):
    today = str(datetime.date.today())
    year,month,date = today.split("-")
    status = rs_privat_module.fastping(config["url"])

    rs_privat_module.check_and_create_folder("Logs")
    rs_privat_module.check_and_create_folder("Logs" + "/" + year + "-" + month)
    
    if status:
        if last == 0:
            rs_privat_module.Log_to_file("Connected", 0, ("Logs" + "/" + year + "-" + month), (today + ".log"), True, True)
            last = 2
        elif last == 1:
            stop = time()
            downtime = stop - start
            rs_privat_module.Log_to_file(("Connection restored" + " | Downtime " + str(int(downtime))), 1, ("Logs" + "/" + year + "-" + month), (today + ".log"), True, True)
            last = 0
            if(os.path.exists("Logs/data.json")):
                new_downtime = int(downtime) + int((rs_privat_module.import_json("Logs/data.json"))["Downtime"])
                date = (rs_privat_module.import_json("Logs/data.json"))["started_at"]
            else:
                new_downtime = int(downtime)
                date = today
            export = {"Downtime" : str(new_downtime), "started_at" : date}
            rs_privat_module.export_json("Logs/data.json", export, False)

    else:
        if last == 0 or last == 2:
            if rs_privat_module.fastping("192.168.0.1"):
                start = time()
                rs_privat_module.Log_to_file("Connection lost", 2, ("Logs" + "/" + year + "-" + month), (today + ".log"), True, True)
                last = 1
            else:
                rs_privat_module.Log_to_file("Connection lost. No connection to gateway.", 1, ("Logs" + "/" + year + "-" + month), (today + ".log"), True, True)

    sleep(5)

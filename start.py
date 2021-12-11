import rs_privat_module
import datetime
from time import sleep

config = rs_privat_module.import_json("config.json")

last = 0

while(True):
    status = rs_privat_module.fastping(config["url"])
    
    if status:
        if last == 0:
            rs_privat_module.Log_to_file("Connected", 0, "Logs", (str(datetime.date.today()) + ".log"), True, False)
        elif last == 1:
            rs_privat_module.Log_to_file("Connection restored", 1, "Logs", (str(datetime.date.today()) + ".log"), True, True)
            last = 0

    else:
        if last == 0:
            rs_privat_module.Log_to_file("Connection lost", 2, "Logs", (str(datetime.date.today()) + ".log"), True, True)
            last = 1

    sleep(5)
import rs_privat_module
import datetime
from time import sleep, time
import os
try:
    import keyboard
    print('Stop the script bye pressin "q".')
except:
    print('Module "Keyboard" is missing. You cant stop the script without an exception. You can install the Module bye typing "pip install keyboard" in the command prompt.')

config = rs_privat_module.import_json("config.json")

if not os.path.exists("Logs"):
    os.makedirs("Logs")

last = 0
downtime = 0 

while(True):
    status = rs_privat_module.fastping(config["url"])
    
    if status:
        if last == 0:
            rs_privat_module.Log_to_file("Connected", 0, "Logs", (str(datetime.date.today()) + ".log"), True, False)
        elif last == 1:
            stop = time.time()
            downtime = stop - start
            rs_privat_module.Log_to_file(("Connection restored" + " | Downtime " + downtime), 1, "Logs", (str(datetime.date.today()) + ".log"), True, True)
            last = 0

    else:
        if last == 0:
            start = time()
            rs_privat_module.Log_to_file("Connection lost", 2, "Logs", (str(datetime.date.today()) + ".log"), True, True)
            last = 1

    sleep(5)

    if keyboard.read_key() == "q":
        break
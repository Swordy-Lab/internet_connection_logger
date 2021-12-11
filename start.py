import rs_privat_module
import datetime
from time import sleep

last = 0

while(True):
    status = rs_privat_module.fastping("google.de")
    
    if status:
        print("Connected")
        if last == 1:
            rs_privat_module.Log_to_file("Connection restored", 0, "Logs", (str(datetime.date.today()) + ".log"))
            last = 0

    else:
        if last == 0:
            rs_privat_module.Log_to_file("Connection lost", 1, "Logs", (str(datetime.date.today()) + ".log"))
            last = 1

    sleep(5)
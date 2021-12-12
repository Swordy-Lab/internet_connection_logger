import os
from datetime import datetime
import json

def Log_to_file (message, status, path, logname, write_to_log, write_to_file):
    if os.path.isfile(os.path.join(path, logname)):
        file = open(os.path.join(path, logname), "r").read()
        if(file == ""):
            is_break = ""
        else:
            is_break = "\n"
    else:
        file = ""
        is_break = ""
        
    switch = {
        0 : "INFO",
        1 : "WARN",
        2 : "ERROR"
    }
    if(status not in switch.keys()):
        current_status = "n/a"
    else:
        current_status = switch[status]
    date = datetime.today().strftime('%d.%m.%Y')
    now = (datetime.now()).strftime("%H:%M:%S")
    entry = (now + " " + date + " | " + current_status + " | " + message)
    if write_to_file:
        file_save = open(os.path.join(path, logname), "w")
        file_save.write(file + is_break + entry)
        file_save.close

    if write_to_log:
        print(entry)

def fastping (hostname):
    if os.name == 'nt':
        response = os.system('ping -n 1 -w 2999 ' + hostname + " > trash.txt")
        os.remove("trash.txt")
    else:
        response = os.system("ping -c 1 " + hostname + " >/dev/null")

    if response == 0:
        return True
    else:
        return False

def import_json (filepath):
    return json.loads((open(filepath, "r", encoding="utf-8")).read())

def export_json (filepath, json_to_export, append):
    if append and os.path.isfile(filepath):
        json_temp = (json.loads((open(filepath, "r", encoding="utf-8")).read()))
        for item_dict in json_to_export:
            if not(item_dict in json_temp):
                json_temp.append(item_dict)
        with open(filepath, 'w', encoding="utf-8") as out_file:
            json.dump(json_temp, out_file)
    else:
        with open(filepath, 'w', encoding="utf-8") as out_file:
            json.dump(json_to_export, out_file)    

version = 1.4
info = "Log_to_file", "fastping", "import_json", "export_json"
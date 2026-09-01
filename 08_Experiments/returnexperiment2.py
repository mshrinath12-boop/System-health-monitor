import json
import psutil
import time
file= open("config.json")
data= json.load(file)
def check_resource(resource_name,value,Critical,Warning):
    if value>=Critical:
        print(f"{resource_name} is in Critical state: {value}%")
        return "Critical"
    elif value>= Warning:
        print(f"{resource_name} is in warning state: {value}%")
        return "Warning"
    else:
        print(f"{resource_name} is in normal state: {value}%")
        return "Normal"
while True:
    from datetime import datetime
    current_time= datetime.now()
    print(current_time)
    cpu= psutil.cpu_percent()
    state= check_resource(
        "Cpu",
         cpu,
        data["cpu_critical"],
         data["cpu_warning"],
    )
    print(state)
    time.sleep(5)
    ram= psutil.virtual_memory().percent
    state= check_resource(
        "Ram",
        ram,
        data["cpu_critical"],
        data["ram_warning"],
    )
    print(state)
    time.sleep(5)
    disk= psutil.disk_usage("c://").percent
    state= check_resource(
        "Disk",
        disk,
        data["disk_critical"],
        data["disk_warning"],


    )
    print(state)
    time.sleep(5)




import json
import psutil
import time
file= open("config.json")
data= json.load(file)
def check_resource(resource_name,value,critical,warning):
    if value>=critical:
        print(f"{resource_name} is in critical state: {value}%")
    elif value>=warning:
        print(f"{resource_name} is in warning state: {value}%")
    else:
        print(f"{resource_name} is in normal state: {value}%")
while True:
    from datetime import datetime
    current_time= datetime.now()
    print(current_time)
    cpu= psutil.cpu_percent()
    check_resource(
        "Cpu",
        cpu,
        data["cpu_critical"],
        data["cpu_warning"],
        )
    time.sleep(5)
    ram= psutil.virtual_memory().percent
    check_resource(
        "Ram",
        ram,
        data["ram_critical"],
        data["ram_warning"],
        )
    time.sleep(5)
    disk= psutil.disk_usage("c:\\").percent
    check_resource("Disk",
                   disk,
                   data["disk_critical"],
                   data["disk_warning"],
                   )
    time.sleep(5)
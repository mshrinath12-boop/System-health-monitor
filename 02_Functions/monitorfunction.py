import json
import psutil
import time
file= open("config.json")
data= json.load(file)
while True:
    from datetime import datetime
    current_time= datetime.now()
    print(current_time)
    def check_cpu():
        cpu= psutil.cpu_percent()
        if cpu >= data["cpu_critical"]:   
            print(f"Cpu is in critical state: {cpu}%")
        elif cpu>= data["cpu_warning"]:
            print(f"Cpu is in warning state: {cpu}%")
        else:
            print(f"Cpu is in normal state: {cpu}%")
    check_cpu()  
    time.sleep(data["interval"])   
    def check_ram():
        ram= psutil.virtual_memory().percent
        if ram>=data["ram_critical"]:
            print(f"Ram is in critical state: {ram}%")
        elif ram>=data["ram_warning"]:
            print(f"Ram is in warning state: {ram}%")
        else:
            print(f"Ram is in normal state: {ram}%")
    check_ram()
    time.sleep(data["interval"])
    def check_disk():
        disk= psutil.disk_usage("c:\\").percent 
        if disk>=data["disk_critical"]:
            print(f"Disk is in critical state: {disk}%")
        elif disk>=data["disk_warning"]:
            print(f"Disk is in warning state: {disk}%")
        else:
            print(f"Disk is in normal state: {disk}%")   
    check_disk()
    time.sleep(data["interval"])
    




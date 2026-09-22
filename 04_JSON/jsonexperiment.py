import json
import psutil
import time
import shutil
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parent / "config.json"

with CONFIG_PATH.open("r", encoding="utf-8") as file:
    data = json.load(file)
while True:
    pass
    from datetime import datetime
    current_time= datetime.now()
    print(current_time)
    cpu= psutil.cpu_percent()
    if cpu>= data["cpu_critical"]:
        print(f"Cpu is in critical state: {cpu}%")
    elif cpu>= data["cpu_warning"]:
        print(f"Cpu is in warning state: {cpu}%")
    else:
        print(f"Cpu is in normal state: {cpu}%")
        time.sleep(data["interval"])
    ram= psutil.virtual_memory().percent
    if ram>=data["ram_critical"]:
         print(f"Ram is in crtical state: {ram}%")
    elif ram>=data["ram_warning"]:
        print(f"Ram is in warning state: {ram}%")
    else:
        print(f"Ram is in normal state: {ram}%")
        time.sleep(data["interval"])
    disk= psutil.disk_usage("/").percent
    if disk>=data["disk_critical"]:
        print(f"Disk is in critical state: {disk:.2f}%")
    elif disk>=data["disk_warning"]:
        print(f"Disk is in warning state: {disk:.2f}%")
    else:
        print(f"Disk is in normal state: {disk:.2f}%")   
        time.sleep(data["interval"])
        


        



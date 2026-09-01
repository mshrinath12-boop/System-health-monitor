import psutil
import logging
import time
logging.basicConfig(
    filename= "system.log",
    level= logging.INFO,
    format= "%(asctime)s | %(levelname)s | %(message)s"
)
def check_resource(resource_name,value,Critical,Warning):
    if value>=Critical:
        logging.critical(f"{resource_name} is in critical state: {value}%")
        return "Critical"
    elif value>=Warning:
        logging.warning(f"{resource_name} is in warning state: {value}%")
        return "Warning"
    else:
        logging.info(f"{resource_name} is in normal state: {value}%")
        return "Normal"
while True:
    from datetime import datetime
    current_time= datetime.now()
    print(current_time)
    cpu= psutil.cpu_percent()
    state= check_resource("Cpu",cpu,90,80)
    print(state)
    time.sleep(5)
    ram= psutil.virtual_memory().percent
    state= check_resource("Ram",ram,90,80)
    print(state)
    time.sleep(5)
    disk= psutil.disk_usage("c:\\").percent
    state= check_resource("Disk",disk,90,80)
    print(state)
    time.sleep(5)

import psutil
import logging
import time
logging.basicConfig(
    filename= "system.log",
    level= logging.INFO,
    format= "%(asctime)s | %(levelname)s | %(message)s "
)
def check_resource(resource_name,value,critical,warning):
        if value>=critical:
            logging.critical(f"{resource_name} is in critical state: {value}%")
        elif value>=warning:
            logging.warning(f"{resource_name} is in warning state: {value}%")
        else:
            logging.info(f"{resource_name} is in normal state: {value}%")
while True:
    from datetime import datetime
    current_time= datetime.now()
    print(current_time)
    cpu= psutil.cpu_percent()
    check_resource("Cpu",cpu,90,80)    
    time.sleep(5)  
    ram= psutil.virtual_memory().percent
    check_resource("Ram",ram,90,80)         
    time.sleep(5)
    disk= psutil.disk_usage("c:\\").percent
    check_resource("Disk",disk,90,80)
    time.sleep(5)


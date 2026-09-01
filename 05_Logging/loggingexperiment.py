import psutil
import logging
import time
logging.basicConfig(
    filename="system.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logging.info("Monitoring started")
while True:
        from datetime import datetime
        current_time= datetime.now()
        print(current_time)
        cpu= psutil.cpu_percent()
        if cpu>=90:
                logging.critical(f"Cpu is in critical state: {cpu}%")
        elif cpu>=80:
                logging.warning(f"Cpu is in warning state: {cpu}%")
        else:
                logging.info(f"Cpu is in normal state: {cpu}%")
                time.sleep(5)                    
        ram= psutil.virtual_memory().percent
        if ram>=90:
                logging.critical(f"Ram is in critical state: {ram}%")     
        elif ram>=80:
                logging.warning(f"Ram is in warning state: {ram}%")
        else:
                logging.info(f"Ram is in normal state: {ram}%")
                time.sleep(5)        
        disk= psutil.disk_usage("c:\\").percent
        if disk>=90:
                logging.critical(f"Disk is in critical state: {disk}%")
        elif disk>=80:
                logging.warning(f"Disk is in warning state: {disk}%")
        else:
                logging.info(f"Disk is in normal state: {disk}%") 
                time.sleep(5)




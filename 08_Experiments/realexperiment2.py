import psutil
import time
file= open("health_report.txt","a")
while True:
    from datetime import datetime
    current_time= datetime.now()
    print(current_time)
    file.write(f"{current_time}\n")
    cpu= psutil.cpu_percent()
    print(f"Cpu usage is: {cpu}%")
    time.sleep(5)
    file.write(f"Cpu usage is: {cpu}%\n")
    ram= psutil.virtual_memory().percent
    print(f"Ram usage is: {ram}%")
    time.sleep(5)
    file.write(f"Ram usage is: {ram}%\n")
    disk= psutil.disk_usage("c:\\").percent
    print(f"Disk usage is: {disk}%")
    time.sleep(5)
    file.write(f"Disk usage is: {disk}%\n")
    if cpu>=90:
      print(f"Cpu is in critical state: {cpu}%")
      time.sleep(5)
      file.write(f"Cpu is in critical state: {cpu}%\n")
    elif cpu>=80:
         print(f"Cpu is in warning state: {cpu}%")
         time.sleep(5)
         file.write(f"\n Cpu is in warning state: {cpu}%\n")
    else:
        print(f"Cpu is in normal state: {cpu}%")
        time.sleep(5)
        file.write(f"\n Cpu is in normal state: {cpu}%\n")        
        if ram>=90:
            print(f"Ram is in critical state: {ram}%")
            file.write(f"\n Ram is in critical state: {ram}%\n")
        elif ram>=80:
            print(f"Ram is in warning state: {ram}%")
            file.write(f"\n Ram is in warning state: {ram}%\n")
        else:
            print(f"Ram usage is normal: {ram}%") 
            time.sleep(5)
            file.write(f"\n Ram is in normal state: {ram}%\n")
        if disk>=90:
                
                print(f"Disk usage is in Critical state: {disk}%")
                file.write(f"\n Disk is in critical state: {disk}%\n")
        elif disk>=80:
                print(f"Disk usage is in warning state: {disk}%")
                file.write(f"\n Disk is in warning state: {disk}%\n")
        else:
                print(f"Disk usage is in normal state: {disk}%")
                time.sleep(5)
                file.write(f"\n Disk is in normal state: {disk}%\n")
                print(f"............................\n")
                file.flush()









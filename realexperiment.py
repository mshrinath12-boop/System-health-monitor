import psutil
def cpu_percent():
    cpu= psutil.cpu_percent(interval=1)
    print(f"Cpu usage: {cpu}%")
cpu_percent()
cpu_percent()
cpu_percent()
cpu= (psutil.cpu_percent(interval=1))
if cpu>=90:
    print(f"Cpu usage is in Critical state: {cpu}%")
if cpu>=80:
    print(f"Cpu usage is in warning state: {cpu}% ")
else:
    print(f"Cpu usage is in normal state: {cpu}%")  
def Ram_percent():
    ram= (psutil.virtual_memory().percent)
    print(f"Ram usage: {ram}%")
Ram_percent()
Ram_percent()
Ram_percent()    
ram= (psutil.virtual_memory().percent)
if ram>=90:
    print(f"Ram usage is in Critical state: {ram}%")
elif ram>=80:
    print(f"Ram usage is in warning state: {ram}%")
else:
    print(f"Ram usage is in normal state: {ram}%")      
def disk_usage():
    disk= psutil.disk_usage("c:\\").percent
    print(f"Disk usage: {disk}%")
disk_usage()
disk_usage()
disk= psutil.disk_usage("c:\\").percent
if disk>=90:
    print(f"Disk usage is in critical state: {disk}%")
elif disk>=80:
    print(f"Disk usage is in warning state: {disk}%")
else:
    print(f"Disk usage is in normal state: {disk}%")     
print(".............")
print(f"System health check : Ram Disk and Cpu usage ") 
print("..............")
print(f"Cpu Usage: {cpu}%")
if cpu>=90:
    print(f"Cpu usage: {cpu}% [critical]")
elif cpu>=80:
    print(f"Cpu usage: {cpu}% [Warning]")
else:
    print(f"Cpu usage: {cpu}% [Normal]")        
print(f"Ram Usage: {ram}%")
if ram>=90:
    print(f"Ram usage: {ram}% [Critical]")
elif ram>=80:
    print(f"Ram usage: {ram}% [Warning]")
else:
    print(f"Ram usage: {ram}% [Normal]")
            
print(f"Disk Usage: {disk}%")
if disk>=90:
    print(f"Disk usage: {disk}% [Critical]")
elif disk>=80:    
    print(f"Disk usage: {disk}% [Warning]")
else:
    print(f"Disk usage: {disk}% [Normal]")
        











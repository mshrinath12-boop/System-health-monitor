import psutil
from colorama import Fore,Style,init
print(".........................................")
print("System health report")
datetime import datetime
current_time= datetime.now()
print(current_time)
cpu= psutil.cpu_percent()
print(f"Cpu usage is: {cpu}%")
if cpu>=90:
        print(f"Status: {Fore.RED}🔴 Critical{Style.RESET_ALL}")
elif cpu>=80:
    print(f"Status: {Fore.YELLOW}🟡 Warning{Style.RESET_ALL}")
else:
    print(f"Status: {Fore.GREEN}🟢 Healthy{Style.RESET_ALL}")
    ram= psutil.virtual_memory().percent    
    print(f"Ram usage is: {ram}%")
if ram>=90:
     print(f"Status: {Fore.RED} 🔴 Critical{Style.RESET_ALL}")
elif ram>=80:
     print(f"Status: {Fore.YELLOW} 🟡 Warning{Style.RESET_ALL}")
else:
     print(f"Status: {Fore.GREEN} 🟢 Healthy{Style.RESET_ALL}")
disk= psutil.disk_usage("c:\\").percent
print(f"Disk usage is: {disk}%")
if disk>=90:
     print(f"Status: {Fore.RED} 🔴 Critical{Style.RESET_ALL}")
elif disk>=80:
     print(f"Status: {Fore.YELLOW} 🟡Warning{Style.RESET_ALL}")
else:
     print(f"Status: {Fore.GREEN} 🟢 Healthy{Style.RESET_ALL}") 
print("....................................................")
             






    
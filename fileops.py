file= open("report.txt","w")
file.write(f"System heath check: ram cpu and disk usage check\n")
cpu= 11
file.write(f"Cpu usage: {cpu}%\n")
ram= 83
file.write(f"Ram usage: {ram}%\n")
disk= 23
file.write(f"Disk usage: {disk}%\n")
if cpu>=90 or  ram>=90 or  disk>=90:
    file.write(f"System health is in critical state\n")
elif cpu>=80 or ram>=80 or disk>=80:
    file.write(f"System health is in warning state\n")
else:          
    file.write(f"System health is in normal state\n")

    
           

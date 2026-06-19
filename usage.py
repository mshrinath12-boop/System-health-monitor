cpu= 82
disk= 85
if cpu>90:
    print(f"Cpu Usage is Critical state: {cpu}%")

elif cpu>80:
    print(f"CpU Usage is in warning state: {cpu}%")
else:
    print(f"Cpu usageis in normal state: {cpu}%")
if disk>90:
    print(f"Disk Usage is in Critical state: {disk}% ")

elif disk>80:
    print(f"Disk Usage is in Warning state: {disk}%")
else:
    print(f"Disk Usage is in Normal state: {disk}%") 
       







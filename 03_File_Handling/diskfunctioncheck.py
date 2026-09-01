import psutil
for item in dir(psutil):
    if "disk" in item.lower():
        print(item)
        print(psutil.disk_usage("c:\\"))
        
                                
                        
      
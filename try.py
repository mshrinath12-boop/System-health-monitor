try:
    threshold=int(input("Enter a cpu threshold: "))
    print(f"Cpu threshold set to: {threshold}%")
except:
    threshold=70
    print("Invalid threshold value")
    print(f"Using default threshold: {threshold}%")

finally:
    print("Program finished")    
    


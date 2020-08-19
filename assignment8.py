while True:
    leap = int(input("Enter a year(yyyy): "))
    if (leap % 4):
        print(f"{leap} is not a leap year") 
    elif not (leap % 100) and (leap % 400):
        print(f"{leap} is not a leap year") 
    elif not (leap % 400):
        print(f"{leap} is a leap year") 
        break
    elif not (leap % 4) and (leap % 100):
        print(f"{leap} is a leap year")
        break 
    
    """this is a leap year assignment"""
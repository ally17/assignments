while True:
    number = input("Enter a number: ")
    num_list = list(number)
    num_len = len(number)
    num_total = 0
    if number.isdigit():
        for i in num_list:
            num_total += int(i) ** num_len
        if num_total == int(number):   
            print(f"{number} is an Armstrong number")
            break
        else:
            print(f"{number} is not an Armstrong number")
    else:
        print(" It is an invalid entry. Don't use non-numeric, float, or negative values!")
    

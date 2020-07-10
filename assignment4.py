while True:
    number = int(input("Enter a number: "))
    prime_list = []
    for i in range(2, number - 1):
       prime = number % i
       prime_list.append(prime)
    if 0 in prime_list:
        print(f"output : {number} is not a prime number")
    else:
        print(f"output : {number} is a prime number")
        break 
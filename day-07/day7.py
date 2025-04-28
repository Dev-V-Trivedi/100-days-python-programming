num = int(input("Enter a number: "))

if num >= 0:  
    if num % 2 == 0:  
        print(f"{num} is positive and even.")
    else:
        print(f"{num} is positive and odd.")
else:
    if num % 2 == 0:  
        print(f"{num} is negative and even.")
    else:
        print(f"{num} is negative and odd.")

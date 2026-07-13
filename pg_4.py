number = int(input("enter a number greater than 1: "))
if number <2:
    print("please enter a greater than 1")
else:
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
                print(f"{number} is  a prime number")
    else:
                print(f"{number} is not a prime number")
def checkprime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(number, "is a not prime number")
                break

        else:
            print(number, "it is a prime number")
    else:
        print(number,"it is not a prime number")



data = int(input("Enter the number to check prime or not: "))
checkprime(data)


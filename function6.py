# factorial
#


def factorial(num):
    fact = 1
    if num < 0:
        return "Invalid Input"
    elif num == 0:
        return 1
    else:
        for i in range(1, num + 1):
            fact = fact * i
        print(fact)


data = int(input("Enter the number to find the facorial: "))
factorial(data)


# n = 5
# factorial = 1
# if n < 0:
#     print("invalid input")
# elif n == 0:
#     print("1")
# else:
#     for i in range(1, n+1):
#         factorial = factorial * i
#     print(factorial)
#








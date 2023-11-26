# 0, 1,1,2,3,5,8...

# def fibonacci(n):
#     if n < 0:
#         return "Invalid Input"
#     elif n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# data = int(input("Enter the number to get fibonacci range: "))
# print(fibonacci(data))

n = int(input("Enter the number to get fibonacci range:",))
n1, n2 = 0, 1
new_number = n2
count = 1
while count < n:
    print(new_number, end=" ")
    count += 1
    n1, n2 = n2, new_number
    new_number = n1 + n2
print()





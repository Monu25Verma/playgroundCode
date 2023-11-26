# amicable  numbers are does number hows divisor of first number is total to get second number and visasversa


# def check_amicable_number(num1, num2):
#     sum1 = 0
#     sum2 = 0
#     for i in range(1, int(num1/2) + 1):
#         if num1 % i == 0:
#             sum1 = sum1 + i
#
#     for i in range(1, int(num2/2)+ 1):
#         if num2 % i == 0:
#             sum2 = sum2 + i
#
#     if sum1 == num2 and sum2 == num1:
#         print("the proper division of",num1, "are", "whose sum is", num2)
#     else:
#         print("it is not a ambical number")
#
#
# check_amicable_number(220, 284)

#
# x=220
# y=280
# sum1=0
# sum2=0
# for i in range(1,x):
#     if x%i==0:
#         sum1+=i
# print(sum1)
#
# for j in range(1,y):
#     if y%j==0:
#         sum2+=j
# print(sum2)

# for num in range(200 , 401):
#     sum1 = 0
#     for i in range(1 , num + 1):
#         if num % i == 0:
#             print(num)
#     # for num2 in range(200 , 401):
#     #     sum2 = 0
#     #     for j in range(1 , num2 + 1):
#     #         if num2 % j == 0:
#     #             sum2 += j
#     # if sum1 == num2 and sum2 == num:
#     #     print("{} and {} are amicable numbers.".format(num, num2))

import math

def divisorGenerator(n1, n2):
    large_idivisors = []
    large_jdivisors = []
    for i in range(1, int(math.sqrt(n1))+1):
        if n1 % i == 0:
            yield i
            if i*i != n1:
                large_idivisors.append(n1 // i)
    for divisor in reversed(large_idivisors):
        yield divisor

    for j in range(1, int(math.sqrt(n2)+1)):
        if n2 % j == 0:
            yield j
            if j*j != n2:
                large_idivisors.append(n2 // j)
    for divisor in reversed(large_jdivisors):
        yield divisor
n1 = 220
n2 = 284
print("the proper division of",220, "are", list(divisorGenerator(n1, 0)),"whose sum is", 284)
print("the proper division of",284, "are", list(divisorGenerator(n2, 0)),"whose sum is", 220)

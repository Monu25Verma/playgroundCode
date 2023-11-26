#12321
def is_palindrom(num):
    num = str(num)
    n = num[::-1]
    if n == num:
        print(num, " is a palindrom number")
    else:
        print(num, " is not a palindrom number")
number = 123
is_palindrom(number)



# n = 1345
# n1 = str(n)
# n2 = n1[::-1]
# if n1== n2:
#     print("yes")
# else:
#     print("no")
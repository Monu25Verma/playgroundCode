#check strong number
#145
#1! = 1
# 4! = 24
# 5! = 120
#1+24+120 -> 145

# def check_strong_number(num):
#     if num ==0 or num == 1:
#         return 1
#     elif num < 0:
#         return "Invalid Number"
#     else:
#         for i in range(2, num+1):
#
#
#
#
# check_strong_number(145)
sum  = 0
num = 145
temp = num
while num:
    i = 1
    fact = 1
    rem = num % 10
    while i <= rem:
        fact = fact * i
        i += 1

    sum = sum + fact
    num = num // 10
if sum == temp:
    print("strong number")
else:
    print("not strong number")





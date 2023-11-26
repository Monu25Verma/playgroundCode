def maxelement(a,b,c):
    if a > b:
        print(a, "is maximum number")
    elif c > b:
        print(c, "is maximum number")
    else:
        print(b, "is maximum number")


a = int(input("enter your value1 to find max number: "))
b = int(input("enter your value2 to find max number: "))
c = int(input("enter your value3 to find max number: "))
maxelement(a, b, c)

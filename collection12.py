#fibonacci series

def generatefibanacci(n):
    n1 = 0
    n2 = 1
    newgenerated = n2
    count = 1
    while count < n:
        print(newgenerated, end=" ")
        count += 1
        n1, n2 = n2, newgenerated
        newgenerated = n1 + n2
    print(newgenerated)

generatefibanacci(15)
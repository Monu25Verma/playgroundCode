def numword(input):
    count = 0
    s1 = input.split()
    for i in s1:
        count += 1
    print(count)

data = 'the sun rises in the east'
numword(data)
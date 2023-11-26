year = []
n = 2012
count = 0
while count < 15:
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        year.append(n)
        count += 1
        n += 4
print(year)
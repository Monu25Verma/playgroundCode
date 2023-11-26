def proper_divisors(num):
    for i in range(1, num):
        if num %i == 0:
            print(i, end = ", ")

proper_divisors(220)
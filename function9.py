def right_shift(nums, n):
    for i in range(n+1):
        data = nums >> i
    print(data)

right_shift(60, 2)
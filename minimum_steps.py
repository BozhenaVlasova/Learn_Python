def minimum_steps(numbers, value):
    arr = sorted(numbers)
    i = 0
    a = arr[i]
    while a < value:
        i += 1
        a += arr[i]
    print(i)





minimum_steps([4,6,3], 7)
# 1
minimum_steps([10,9,9,8], 17)
# 1
minimum_steps([8,9,10,4,2], 23)
# 3
minimum_steps([19,98,69,28,75,45,17,98,67], 464)
# 8
minimum_steps([4,6,3], 2)
# 0
import math

def count_specMult(n, max_val):
    simple_list = []
    count = 0
    result_list = []

    for i in range(2, max_val+1):
        if count == n:
            break
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            simple_list.append(i)
            count += 1

    mul = math.prod(simple_list)
    for i in range(mul, max_val, mul):
        result_list.append(i)

    print(len(result_list))



count_specMult(3, 200)
# 6
count_specMult(3, 1000)
# 33
count_specMult(4, 500)
# 2
count_specMult(4, 1000)
# 4
count_specMult(2, 100)
# 16
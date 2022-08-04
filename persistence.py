def mult(value):
    mul = 1
    while (value != 0):
        mul *= value % 10
        value = value // 10
    n = mul
    return n


def persistence(n):
    if len(str(n)) == 1:
        print(0)
    else:
        a = mult(n)
        count = 1
        while len(str(a)) != 1:
            count +=1
            a = mult(a)
            mult(a)
        else:
            print(count)


persistence(39)
# 3
persistence(4)
# 0
persistence(25)
# 2
persistence(999)
# 4
persistence(408659)
# 1
def min_value(digits):
    arr = sorted(set(digits))
    val = ""
    for i in arr:
        val += "".join(str(i))
    print(int(val))


min_value([1, 3, 1]) #13
min_value([4, 7, 5, 7]) #457
min_value([4, 8, 1, 4]) #148
def list_depth(l):
    l = str(l)
    count = 0
    max_depth = 0
    for i in l:
        if i == '[':
            count+=1
        if i == ']':
            count-=1
        if count > max_depth:
            max_depth = count
    print(max_depth)


list_depth([1, [2, [3, [4, [5, [6], 5], 4], 3], 2], 1])
# 6
list_depth([True])
# 1
list_depth([])
# 1
list_depth([2, "yes", [True, False]])
# 2
list_depth([2.0, [2, 0], 3.7, [3, 7], 6.7, [6, 7]])
# 2
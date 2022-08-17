import itertools as it

def est_subsets(arr):
    sum = 0
    count = 1
    set_list = []
    while count <= len(arr):
        a = it.combinations(arr, count)
        for i in a:
            j = sorted(set(i))
            if j not in set_list:
                set_list.append(j)
                sum += 1
        count += 1
    print(sum)


est_subsets([1, 2, 3, 4])
# 15
est_subsets(['a', 'b', 'c', 'd', 'd'])
# 15
est_subsets([2, 3, 4, 5, 5, 6, 6, 7, 8, 8])
# 127
est_subsets(['a', 'z', 'z', 'z', 'b', 'j', 'f', 'k', 'b', 'd', 'j', 'j', 'n', 'm', 'm'])
# 511
est_subsets([1] * 8)
# 1
est_subsets([])
# 0
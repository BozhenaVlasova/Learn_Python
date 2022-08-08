def bonus(arr, s):
    min_val = min(arr)
    val = []
    result = []
    for i in arr:
        val.append((i/min_val)**-1)
    
    sum_val = sum(val)
    for v in val:
        result.append(round(s*v/sum_val))
    print(result) 


bonus([18, 15, 12], 851)
# [230, 276, 345]
bonus([22, 3, 15], 18228)
# [1860, 13640, 2728]
bonus([8, 14, 11], 23541)
# [10241, 5852, 7448]
bonus([8, 20, 17], 25281)
# [13515, 5406, 6360]
bonus([25, 22, 15, 22, 22], 5213)
# [858, 975, 1430, 975, 975]
bonus([10, 11, 30, 12, 17, 23, 30, 11, 17, 10], 1788210)
# [258060, 234600, 86020, 215050, 151800, 112200, 86020, 234600, 151800, 258060]
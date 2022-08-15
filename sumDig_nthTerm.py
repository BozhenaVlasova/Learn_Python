def sumDig_nthTerm(initVal, patternL, nthTerm):
    count = 1
    i = 0
    while count < nthTerm:
        if len([initVal]) <= nthTerm:
            if i >= len(patternL):
                i = 0
            initVal += patternL[i]
            [initVal].append(initVal)
            count += 1
            i += 1
    a = [initVal][-1]
    summ = 0
    while (a != 0):
        summ += a % 10
        a = a // 10
    a = summ
    print(summ)



sumDig_nthTerm(10, [2, 1, 3], 6)
# 10
sumDig_nthTerm(10, [2, 1, 3], 15)
# 10
sumDig_nthTerm(10, [2, 1, 3], 50)
# 9
sumDig_nthTerm(10, [2, 1, 3], 78)
# 10
sumDig_nthTerm(10, [2, 1, 3], 157)
# 7
sumDig_nthTerm(10, [2, 2, 5, 8], 6)
# 11
sumDig_nthTerm(10, [2, 2, 5, 8], 15)
# 11
sumDig_nthTerm(10, [2, 2, 5, 8], 50)
# 9
sumDig_nthTerm(10, [2, 2, 5, 8], 78)
# 11
sumDig_nthTerm(10, [2, 2, 5, 8], 157)
# 16
sumDig_nthTerm(100, [2, 2, 5, 8], 6)
# 11
sumDig_nthTerm(100, [2, 2, 5, 8], 15)
# 11
sumDig_nthTerm(100, [2, 2, 5, 8], 50)
# 9
sumDig_nthTerm(100, [2, 2, 5, 8], 78)
# 11
sumDig_nthTerm(100, [2, 2, 5, 8], 157)
# 16
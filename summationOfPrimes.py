def summationOfPrimes(primes):
    l = []
    for i in range(2, primes+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            l.append(i)
    print(sum(l))


summationOfPrimes(10)
# 17
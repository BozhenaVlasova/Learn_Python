def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

def minimum_number(numbers):
    a = sum(numbers)
    b = 0
    while isprime(a) == False:
        b+=1
        a+=1
    print(b)



minimum_number([3,1,2])
# 1
minimum_number([5,2])
# 0
minimum_number([1,1,1])
# 0
minimum_number([2,12,8,4,6])
# 5
minimum_number([50,39,49,6,17,28])
# 2
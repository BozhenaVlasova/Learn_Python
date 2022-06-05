def min_sum(arr):
    a = sorted(arr)
    arr.sort(reverse = True)
    arr3 = []
    for i in range(int(len(arr)/2)):
        arr3.append(arr[i]*a[i])
    print(sum(arr3))
        


min_sum([5,4,2,3])
min_sum([12,6,10,26,3,24])
min_sum([9,2,8,7,5,4,0,6])
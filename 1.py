arr = [1, 2, 5, 6, 5, 2, 22]

a = dict.fromkeys(arr)

for i in arr:
    a[i] = 0

for i in arr:
    for j in arr:
        if i == j:
            a[i] = a[i] +1 
            break

for i in sorted(a):
    if a[i] >= 2:
        print(i, a[i])
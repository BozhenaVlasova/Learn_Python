import string
f = {}
for i,j in enumerate(string.ascii_lowercase):
    f[f'{j}'] = i+1

def encode(message, key):

    arr1 = []
    arr2 = []
    arr3 = []

    for i in message:
        arr1.append(f[f"{i}"])

    for j in str(key):
        arr2.append(int(j))

    a = len(arr1) - len(arr2)

    c= 0
    while len(arr1) != len(arr2):
        arr2.append(int(str(key)[c]))
        c+=1
        if c == len(str(key)):
            c = 0
    for n in range(len(message)):
        arr3.append(arr1[n]+arr2[n])
    print(arr3)

encode("scout", 1939)
#encode("masterpiece", 1939)

input()
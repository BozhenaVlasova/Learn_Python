def row_weights(array):
    arr1 = []
    arr2 = []
    for i,x in enumerate(array):
        if i%2 == 0:
            arr1.append(x)
        else:
            arr2.append(x)
    print((sum(arr1), sum(arr2)))


row_weights([80]) #(80,0)
row_weights([100,50]) #(100,50)
row_weights([50,60,70,80]) #(120,140)
row_weights([13,27,49]) #(62,27)
row_weights([70,58,75,34,91]) #(236,92)
row_weights([29,83,67,53,19,28,96]) #(211,164)
row_weights([0]) #(0,0)
row_weights([100,51,50,100]) #(150,151)
row_weights([39,84,74,18,59,72,35,61]) #(207,235)
row_weights([0,1,0]) #(0,1)
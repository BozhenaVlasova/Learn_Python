import numpy as np

def delete_nth(order,max_e):
    ll = np.array(order)
    ind_list = []
    val_list = []
    for i in ll:
        ind = np.where(ll == i)[0]
        indd = list(ind)
        ind_list.append(indd)
        val_list.append(i)
    next_order = list(zip(val_list, ind_list))

    arr = []
    arr1 = []
    for j in next_order:
        if j[0] not in arr:
            arr1.append(j)
        arr.append(j[0])

    arr2 = []
    for a in arr1:
        if len(a[1]) > max_e:
            arr2.append(a[1][:max_e])
        else:
            arr2.append(a[1])

    real_list = list(zip(set(arr),arr2))

    end_list = []
    for i,x in enumerate(order):
        for j,n in enumerate(real_list):
            if i in n[1]:
                end_list.append(x)
    print(end_list)

delete_nth([20,37,20,21], 1)
# [20,37,21]
delete_nth([1,1,1,1,1,3,3,7,2,2,2,2], 3)
# [1,1,1,3,3,7,2,2,2]
delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1],3)
# [1, 2, 3, 1, 1, 2, 2, 3, 3, 4, 5]
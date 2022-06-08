# № 1
def adjacent_element_product(array):
    arr2 = []
    for i,x in enumerate(array):
        if i == len(array)-1:
            break
        arr1 = []        
        for j in range(len(array)):
            if i !=j:
                arr1.append(array[i]*array[j])
        arr2.append(arr1[i])
    print(max(arr2))


# № 2
def adjacent_element_product_2(array):
    arr2 = []
    for a,b in zip(array, array[1:]):
        arr2.append(a*b)
    print(max(arr2))


#Positive numbers
adjacent_element_product([5, 8]) 
# 40
adjacent_element_product([1, 2, 3]) 
# 6
adjacent_element_product([1, 5, 10, 9]) 
# 90
adjacent_element_product([4, 12, 3, 1, 5]) 
# 48
adjacent_element_product([5, 1, 2, 3, 1, 4]) 
# 6
    
#Both positive and negative values
adjacent_element_product([3, 6, -2, -5, 7, 3]) 
# 21
adjacent_element_product([9, 5, 10, 2, 24, -1, -48]) 
# 50
adjacent_element_product([5, 6, -4, 2, 3, 2, -23]) 
# 30
adjacent_element_product([-23, 4, -5, 99, -27, 329, -2, 7, -921]) 
# -14
adjacent_element_product([5, 1, 2, 3, 1, 4]) 
# 6

#Contains zeroes
adjacent_element_product([1, 0, 1, 0, 1000]) 
# 0
adjacent_element_product([1, 2, 3, 0]) 
# 6
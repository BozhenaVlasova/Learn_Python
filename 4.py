def product_array(numbers):
    arr = []
    for i, v in enumerate(numbers):
        c = 1
        for j in range(len(numbers)):
            if i != j:
                c *= numbers[j]
        arr.append(c)
    print(arr)


product_array([12,20]) #[20,12]
product_array([12,20]) #[20,12]
product_array([3,27,4,2]) #[216,24,162,324]
product_array([13,10,5,2,9]) #[900,1170,2340,5850,1300]
product_array([16,17,4,3,5,2]) #[2040,1920,8160,10880,6528,16320]
product_array([16,2,4,3,9,2,1])
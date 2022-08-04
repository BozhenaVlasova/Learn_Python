def flatten_and_sort(array):
    array_list = []
    for i in array:
        for j in i:
            array_list.append(j)
    array_list.sort()
    print(array_list)


flatten_and_sort([])
# []
flatten_and_sort([[], []])
# []
flatten_and_sort([[], [1]])
# [1]
flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]])
[1, 2, 3, 4, 5, 6, 7, 8, 9]
flatten_and_sort([[1, 3, 5], [100], [2, 4, 6]])
# [1, 2, 3, 4, 5, 6, 100]
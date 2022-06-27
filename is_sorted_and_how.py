def is_sorted_and_how(arr):
    if arr == sorted(arr):
        print('yes, ascending')
    elif arr == sorted(arr, reverse = True):
        print('yes, descending')
    else:
        print('no')


is_sorted_and_how([1, 2]) # 'yes, ascending'
is_sorted_and_how([15, 7, 3, -8]) # 'yes, descending'
is_sorted_and_how([4, 2, 30]) # 'no'
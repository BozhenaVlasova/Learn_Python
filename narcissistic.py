def narcissistic(value):
    val_list = []
    narc_list = []
    for i in str(value):
        val_list.append(i)
    if len(val_list) == 1:
        print(True)
    else:
        for i in val_list:
            a = int(i)**len(val_list)
            narc_list.append(a)
        if sum(narc_list) == value:
            print(True)
        else:
            print(False)



narcissistic(7)
# True, '7 is narcissistic'
narcissistic(371)
# True, '371 is narcissistic'
narcissistic(122)
# False, '122 is not narcissistic'
narcissistic(4887)
# False, '4887 is not narcissistic'
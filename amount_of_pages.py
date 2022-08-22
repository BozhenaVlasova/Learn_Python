def amount_of_pages(summary):
    sum = 0
    for i in range(1, summary+1):
        sum += len(str(i))
        if sum == summary:
            print(i)



amount_of_pages(5)
# 5
amount_of_pages(25)
# 17
amount_of_pages(1095)
# 401        
amount_of_pages(185)
# 97
amount_of_pages(660)
# 256
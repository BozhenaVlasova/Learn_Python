def mirror(text):
    a = text.split()
    stars = '****'
    j = ''
    b = [i[::-1] for i in a]
    count = max(len(i) for i in b)
    for i in b:
        if len(i) <= count:
            j += '* ' + i +' '*(count - len(i)) + ' *\n'
    stars += '*'*count
    print(stars+'\n'+j+stars)


mirror("Hello World")
# *********\n* olleH *\n* dlroW *\n*********
mirror("Codewars")
# "************\n* srawedoC *\n************"
mirror("emosewA !ataK")
# "***********\n* Awesome *\n* Kata!   *\n***********"
mirror("rwy ov ffeb ujcgaei avfo")
# ***********\n* ywr     *\n* vo      *\n* beff    *\n* ieagcju *\n* ofva    *\n***********
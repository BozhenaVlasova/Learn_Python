def inside_out(st):
    io = st.split(' ')
    st_list = []
    for i in io:
        if len(i)%2==0 and len(i)>3:
            s1 = i[:len(i)//2]
            s2 = i[len(i)//2:]
            st_list.append(''.join(s1[::-1] + s2[::-1]))
        elif len(i)%2 != 0 and len(i)>3:
            s1 = i[:len(i)//2]
            s2 = i[len(i)//2::(len(i)//2)+1]
            s3 = i[(len(i)//2)+1:]
            st_list.append(''.join(s1[::-1]+s2+s3[::-1]))
        else:
            st_list.append(i)
    st_list = ' '.join(st_list)
    print(st_list)



inside_out('man i need a taxi up to ubud')
# 'man i ende a atix up to budu'
inside_out('what time are we climbing up the volcano')
# 'hwta item are we milcgnib up the lovcona'
inside_out('take me to semynak')
# 'atek me to mesykan'
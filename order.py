import re

def order(sentence):
    sent = sorted(zip(re.findall('[0-9]', sentence), sentence.split()))
    sent_list = [i[1] for i in sent]
    print(" ".join(sent_list))


order("is2 Thi1s T4est 3a")
# "Thi1s is2 3a T4est"
order("4of Fo1r pe6ople g3ood th5e the2")
# "Fo1r the2 g3ood 4of th5e pe6ople"
order("")
# ""
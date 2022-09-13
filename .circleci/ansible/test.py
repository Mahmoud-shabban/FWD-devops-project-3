from asyncio.windows_events import NULL
from cmath import nan


l1 = [2,4,3]
l2 = [5,6,4]

def add(l1,l2):
    r = []
    temp = 0
    for i in range(max(len(l1), len(l2))):
        if i < len(l1) and i < len(l2):
            summ = l1[i] + l2[i] + temp
            if summ  >= 10 and i < max(len(l1), len(l2)):
                r.append(summ-10)
                temp = 1
            elif summ < 10 and i < max(len(l1), len(l2)):
                r.append(summ)
                temp = 0
                continue
            else:
                r.append(summ)
        if i > len(l1) :
            summ = temp + l2[i] 
            if summ  >= 10 and i < max(len(l1), len(l2)):
                r.append(summ-10)
                temp = 1
            elif i < 10 and i < max(len(l1), len(l2)):
                r.append(summ)
                temp = 0
                continue
            else:
                r.append(summ)
        if i > len(l2)  :
            summ = temp + l1[i] 
            if summ  >= 10 and i < max(len(l1), len(l2)):
                r.append(summ-10)
                temp = 1
            elif summ < 10 and i < max(len(l1), len(l2)):
                r.append(summ)
                temp = 0
                continue
            else:
                r.append(summ)
    return r
print(add(l1,l2))

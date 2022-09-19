def genlist():
    list = [0,0]
    a = 10
    b = 10
    list[0] = a
    list[1] = b
    return list


print(genlist())

def blist(list):
    return list[0] + list[1]


print(blist(genlist()))


print
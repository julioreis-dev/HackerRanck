
def compareTriplets(a, b):
    listresult = []
    alice = 0
    bob = 0
    tuple1 = a
    tuple2 = b
    for index,n in enumerate(tuple1):
        if tuple1[index]>tuple2[index]:
            alice+=1
        elif tuple1[index]<tuple2[index]:
            bob+=1
        else:
            pass
    listresult.append(alice)
    listresult.append(bob)
    return listresult

x=(17,28,30)
z=(99,16,8)
w = compareTriplets(x, z)
print(w)

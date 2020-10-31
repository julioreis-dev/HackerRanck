def plusMinus(arr):
    list1 = []
    listm1 = []
    list0 = []
    leightg = len(arr)
    for n in arr:
        if n > 0:
            list1.append(n)
        elif n < 0:
            listm1.append(n)
        else:
            list0.append(n)
    print(f'{len(list1)/leightg}\n{len(listm1)/leightg}\n{len(list0)/leightg}')

m = [1, 1, 0, -1, -1]
x = plusMinus(m)
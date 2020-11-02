def diagonalDifference(arr):
    # Write your code here
    listprin = []
    listsecund = []
    for index in range(0, len(arr)):
        line = arr[index]
        x = line[index]
        listprin.append(x)
    for index1 in range(0, len(arr)):
        line1 = arr[index1]
        line1.reverse()
        y = line1[index1]
        listsecund.append(y)
    valor = 0
    for n in listprin:
        valor = valor + n
    valor2 = 0
    for i in listsecund:
        valor2 = valor2 + i
    return abs(valor - valor2)



m = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
print(diagonalDifference(m))

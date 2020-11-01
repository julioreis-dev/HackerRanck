def aVeryBigSum(ar):
    soma = 0
    for n in ar:
        soma = soma + n
    return soma

ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
x = aVeryBigSum(ar)
print(x)

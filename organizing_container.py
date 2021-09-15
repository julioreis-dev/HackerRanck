def organizingcontainer(cont):
    container_capacidade = []
    geral = [0]*len(cont)
    for i in cont:
        container_capacidade.append(sum(i))
        for tipo, quant in enumerate(i):
            geral[tipo] += quant
    # container_capacidade.sort()
    # geral.sort()
    # return container_capacidade, geral
    if sorted(container_capacidade) == sorted(geral):
        return 'Possible'
    return 'Impossible'

array_3new = [[1, 3, 1], [2,1,2], [3,3,3]]
array_3new1 = [[0, 2, 1], [1, 1, 1], [2, 0, 0]]
array_3new2 = [[2, 0, 0], [1, 1, 1], [0, 2, 1]]

array_2new = [[1,1], [1,1]]
array_2new1 = [[0,2], [1,1]]

print(organizingcontainer(array_2new))
print(organizingcontainer(array_2new1))
print()
print(organizingcontainer(array_3new))
print(organizingcontainer(array_3new1))
print(organizingcontainer(array_3new2))


def compar(a: list, b: list):
    if len(a) == len(b):
        if sorted(a) == sorted(b):
            return False
        return True
    return True


def analise_dif(principal: list, subset: list):
    list_result = []
    for n in subset:
        if n in principal:
            list_result.append(True)
        else:
            list_result.append(False)
    if False in list_result:
        return False
    return True


if __name__ == '__main__':
    prc = list(map(int, input().split()))
    lenth = int(input())
    sub = []
    subsets = []
    list_results = []
    for _ in range(lenth):
        subsets = list(map(int, input().split()))
        sub.append(subsets)

    for lista_sub in sub:
        result = compar(prc, lista_sub)
        if result:
            list_results.append(analise_dif(prc, lista_sub))
        else:
            list_results.append(result)
    if False in list_results:
        print(False)
    else:
        print(True)

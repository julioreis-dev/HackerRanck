def passwordCracker(passwords, loginAttempt):
    total = len(loginAttempt)
    eh_possivel = [False]*(total+1)
    eh_possivel[0] = True
    lista_palavra = []
    for posicao in range(total):
        x = eh_possivel[posicao]
        if eh_possivel[posicao] == False:
            continue
        for palavra in passwords:
            y=loginAttempt[posicao:]
            if loginAttempt[posicao:].startswith(palavra):
                eh_possivel[posicao+len(palavra)] = True
                lista_palavra.append(palavra)
                break
    if eh_possivel[-1]:
        return ' '.join(lista_palavra)
    return 'WRONG PASSWORD'



# print(passwordCracker(['because', 'can', 'do', 'must', 'we', 'what'], 'wedowhatwemustbecausewecan'))
print(passwordCracker(['ab', 'abcd', 'cd'], 'abcd'))
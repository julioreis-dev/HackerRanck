from time import time


def timeprocess(funcao):
    def calctime(*args, **kwargs):
        v0 = time()
        result = funcao(*args, **kwargs)
        v1 = time()
        temp = v1-v0
        print(temp)
        return result
    return calctime


@timeprocess
def fib(n):
    if n == 0:
        x = 0
    elif n == 1:
        x = 1
    else:
        x = fib(n - 1) + fib(n - 2)
    return x


@timeprocess
def soma(n):
    soma1 = 0
    for i in range(n):
        soma1 = soma1 + 1
    return soma1


number = int(input('Digite um numero: '))
# y = fib(number)
y = soma(number)
print(y)

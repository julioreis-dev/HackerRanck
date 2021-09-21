def create_hash(t):
    final = tuple(t)
    return hash(final)


n = int(input('numero da tupla'))
t = map(int, input().split())
print(create_hash(t))
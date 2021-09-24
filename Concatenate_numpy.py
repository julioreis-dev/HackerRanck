import numpy as np

array_1 = np.array([1,2,3])
array_2 = np.array([4,5,6])
array_3 = np.array([7,8,9])

print (np.concatenate((array_1, array_2, array_3)))

array_3= np.array([[1,2,3],[0,0,0]])
array_4 = np.array([[0,0,0],[7,8,9]])

print (np.concatenate((array_3, array_4), axis = 1))


# Desafio hackerrank
space = list(map(int, input().split()))
n = [list(map(int, input().split())) for _ in range(space[0])]
m = [list(map(int, input().split())) for _ in range(space[1])]
array_n = np.array(n)
array_m = np.array(m)
print(np.concatenate((array_n, array_m), axis=0))



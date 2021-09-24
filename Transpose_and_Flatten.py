import numpy as np

# array = [[1,2,3], [4,5,6]]
#
# my_Array = np.array(array)
# print(np.transpose(my_Array))

n = list(map(int, input().split()))
array = [list(map(int, input().split())) for _ in range(n[0])]
my_array = np.array(array)
print(np.transpose(my_array), my_array.flatten(), sep='\n')

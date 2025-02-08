import numpy as np


#  1D array 
print("1D array")
arr=np.array([1,2,3,4,5,6,7,8])
print(arr[1])

print(arr[:4],"\n\n")


print("2d array examples \n")

# 2D array 

arr_2d=np.array(([1,2,3],[4,5,6]))

# arr_2d[0:2,0:2] starting from 0th row end with 2 rows , starting with 0 element end with 2 index element 
print(arr_2d[0:2,0:2])
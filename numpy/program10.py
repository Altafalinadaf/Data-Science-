import numpy as np

arr1=np.array([[1,2,3]])
arr2=np.array([[4,5,6]])

print('vertical stacking joins arrays column wise')
arr3= np.vstack((arr1,arr2))
print(arr3)

print('horizontal stacking joins arrays column wise')
arr4=np.hstack((arr1,arr2))
print(arr4)


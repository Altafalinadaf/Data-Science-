# Ndim - The ndim attribute gives the number of dimensions (or axes) of the array. This tells you whether the
# array is 1D, 2D, or has more dimensions.

import numpy as np

arr = np.array(([1,2,3],[2,3,4]))
print(arr.ndim)
# Problem: You need to perform calculations on large numerical datasets, such
# as arrays or grids.

# numpy provides an array object which more efficient and better suited for
# mathematical calculations than a standard Python list

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
x * 2 # [1, 2, 3, 4, 1, 2, 3, 4]
x + 10 # TypeError
x + y # [1, 2, 3, 4, 5, 6, 7, 8]

# Numpy arrays
import numpy as np
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
ax * 2 # array([2, 4, 6, 8])
ax + 10 # array([11, 12, 13, 14])
ax + ay # array([6, 8, 10, 12])
ax * ay # array([5, 12, 21, 32])

# scalar operations: apply operations element by element


# The fact that math operations apply to all of the elements simultaneously
# makes it very easy and fast to compute functions across an entire array

def f(x):
    return 3*x**2 - 2*x + 7

f(ax) # array([8, 15, 28, 47])

np.sqrt(ax) # array([ 1. , 1.41421356, 1.73205081, 2. ])
np.cos(ax) # array([ 0.54030231, -0.41614684, -0.9899925 , -0.65364362])

grid = np.zeros(shape=(10000, 10000), dtype=float)
grid
# array([[ 10., 10., 10., ..., 10., 10., 10.],
#          [ 10.,  10.,  10., ...,  10.,  10.,  10.],
#          [ 10.,  10.,  10., ...,  10.,  10.,  10.],
#          ...,
#          [ 10.,  10.,  10., ...,  10.,  10.,  10.],
#          [ 10.,  10.,  10., ...,  10.,  10.,  10.],
#          [ 10.,  10.,  10., ...,  10.,  10.,  10.]])

np.sin(grid)
# array([[-0.54402111, -0.54402111, -0.54402111, ..., -0.54402111,
#           -0.54402111, -0.54402111],
#          [-0.54402111, -0.54402111, -0.54402111, ..., -0.54402111,
#           -0.54402111, -0.54402111],
#          [-0.54402111, -0.54402111, -0.54402111, ..., -0.54402111,
#           -0.54402111, -0.54402111],
#          ...,
#          [-0.54402111, -0.54402111, -0.54402111, ..., -0.54402111,
#           -0.54402111, -0.54402111],
#          [-0.54402111, -0.54402111, -0.54402111, ..., -0.54402111,
#           -0.54402111, -0.54402111],
#          [-0.54402111, -0.54402111, -0.54402111, ..., -0.54402111,
#           -0.54402111, -0.54402111]])
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
a 
# array([[ 1,  2,  3,  4],
       # [ 5,  6,  7,  8],
       # [ 9, 10, 11, 12]])

# Select row 1
a[1] # array([5, 6, 7, 8])

# Select column 1
a[:, 1] # array([2, 6, 10])

# Select a subregion and change it
a[1:3, 1:3]
# array([[ 6, 7],
       # [10, 11]])
a[1:3, 1:3] += 10
a
# array([[ 1, 2, 3, 4],
           # [ 5, 16, 17,  8],
           # [ 9, 20, 21, 12]])

# Broadcast a row vector across an operation on all rows
a + [100, 101, 102, 103]
# array([[101, 103, 105, 107],
       # [105, 117, 119, 111],
       # [109, 121, 123, 115]])

# Conditional assignment on an array
np.where(a < 10, a, 10) # a<10?a:10
# array([[ 1, 2, 3, 4],
       # [ 5, 10, 10,  8],
       # [ 9, 10, 10, 10]])


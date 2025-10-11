import numpy as np

# Q1
A = np.array([[1, 5, 6], [3, 2, 8]])
B = np.array([[4, 8, 9], [10, 7, 12]])

print("Array A:\n", A)
print("Array B:\n", B)

vertical_stack = np.vstack((A, B))
print("Vertical Stack Result:\n", vertical_stack)

horizontal_stack = np.hstack((A, B))
print("Horizontal Stack Result:\n", horizontal_stack)

# Q2
common = np.intersect1d(A, B)
print("Common elements of A and B:", common)

# Q3
indices = np.where((A >= 5) & (A <= 10))
result_where = A[indices]
print("Numbers between 5 and 10 in Array A:", result_where)

# Q4
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

condition1 = iris_2d[:, 0] < 5.0
condition2 = iris_2d[:, 2] > 1.5

filtered_rows = iris_2d[condition1 & condition2]

print("Filter condition: sepallength < 5.0 and petallength > 1.5")
print("Shape of filtered data:", filtered_rows.shape)
print("Filtered data (first 5 rows):\n", filtered_rows[:5])

import numpy as np

print("===== LINEAR ALGEBRA FUNCTIONS =====")

# Arrays and matrices
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# 1. dot()
print("dot():", np.dot(a, b))

# 2. matmul()
print("\nmatmul():\n", np.matmul(A, B))

# 3. determinant
print("\ndet():", np.linalg.det(A))

# 4. inverse
print("\ninv():\n", np.linalg.inv(A))

# 5. eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("\neig() - Eigenvalues:", eigenvalues)
print("eig() - Eigenvectors:\n", eigenvectors)

# 6. singular value decomposition
U, S, V = np.linalg.svd(A)
print("\nsvd() - U:\n", U)
print("svd() - S:", S)
print("svd() - V:\n", V)

# 7. solve linear equations (Ax = b)
b2 = np.array([5, 6])
solution = np.linalg.solve(A, b2)
print("\nsolve():", solution)

# 8. matrix rank
print("\nmatrix_rank():", np.linalg.matrix_rank(A))
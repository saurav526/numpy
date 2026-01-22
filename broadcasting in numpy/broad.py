import numpy as np
print("\n===== VECTORIZATION =====")

# Vectorized operation – Performs element-wise operations without loops
e = np.array([1, 2, 3, 4])
print("Vectorized square (e * e):", e * e)

# vectorize() – Converts a normal Python function into a vectorized function
def square(n):
    return n * n

vec_square = np.vectorize(square)
print("vectorize():", vec_square(e))
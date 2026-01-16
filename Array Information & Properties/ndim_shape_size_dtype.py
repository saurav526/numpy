import numpy as np

print("----- ARRAY CREATION FUNCTIONS -----")

# 1. array()
a = np.array([1, 2, 3, 4, 5])
print("np.array():", a)

# 2. zeros()
b = np.zeros((2, 3))
print("\nnp.zeros():\n", b)

# 3. ones()
c = np.ones((3, 2))
print("\nnp.ones():\n", c)

# 4. empty()
d = np.empty((2, 2))
print("\nnp.empty():\n", d)

# 5. arange()
e = np.arange(1, 10, 2)
print("\nnp.arange():", e)

# 6. linspace()
f = np.linspace(1, 10, 5)
print("\nnp.linspace():", f)

# 7. full()
g = np.full((2, 3), 7)
print("\nnp.full():\n", g)

# 8. eye()
h = np.eye(3)
print("\nnp.eye():\n", h)


print("\n----- ARRAY INFORMATION FUNCTIONS -----")

# Using array 'a' for information
print("Array:", a)
print("ndim (Dimensions):", a.ndim)
print("shape:", a.shape)
print("size (Total elements):", a.size)
print("dtype (Data type):", a.dtype)
print("itemsize (Bytes per element):", a.itemsize)
print("nbytes (Total bytes):", a.nbytes)

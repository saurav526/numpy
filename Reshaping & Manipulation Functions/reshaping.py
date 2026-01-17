# reshape()	Change shape
# flatten()	Convert to 1D
# ravel()	Flatten (view if possible)
# transpose()	Transpose array
# swapaxes()	Swap axes
# concatenate()	Join arrays
# stack()	Stack arrays
# split()	Split array 

import numpy as np
import numpy as np

print("========= ORIGINAL ARRAY =========")
a = np.array([1, 2, 3, 4, 5, 6])
print("Array a:", a)

# ================= RESHAPING FUNCTIONS =================
print("\n========= RESHAPING FUNCTIONS =========")

# 1. reshape()
b = a.reshape(2, 3)
print("\nreshape(2,3):\n", b)

# 2. flatten()
c = b.flatten()
print("\nflatten():", c)

# 3. ravel()
d = b.ravel()
print("\nravel():", d)

# 4. transpose()
e = b.transpose()
print("\ntranspose():\n", e)

# 5. swapaxes()
f = np.swapaxes(b, 0, 1)
print("\nswapaxes(0,1):\n", f)

# 6. expand_dims()
g = np.expand_dims(a, axis=0)
print("\nexpand_dims(axis=0):\n", g)

# 7. squeeze()
h = np.squeeze(g)
print("\nsqueeze():", h)

# 8. concatenate()
i = np.array([7, 8, 9])
j = np.concatenate((a, i))
print("\nconcatenate():", j)

# 9. split()
k = np.split(a, 3)
print("\nsplit():", k)
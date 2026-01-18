import numpy as np

print("===== ORIGINAL ARRAY =====")
a = np.array([10, 20, 30, 40, 50])
b = np.array([15, 20, 25, 40, 60])
print("Array a:", a)
print("Array b:", b)

# ================= STATISTICAL FUNCTIONS =================
print("\n===== STATISTICAL FUNCTIONS =====")

# mean()
print("mean():", np.mean(a))

# median()
print("median():", np.median(a))

# sum()
print("sum():", np.sum(a))

# min()
print("min():", np.min(a))

# max()
print("max():", np.max(a))

# standard deviation
print("std():", np.std(a))

# variance
print("var():", np.var(a))

# argmin()
print("argmin():", np.argmin(a))

# argmax()
print("argmax():", np.argmax(a))

# percentile
print("percentile(50):", np.percentile(a, 50))

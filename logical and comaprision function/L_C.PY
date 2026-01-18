import numpy as np

print("===== ORIGINAL ARRAY =====")
a = np.array([10, 20, 30, 40, 50])
b = np.array([15, 20, 25, 40, 60])
print("Array a:", a)
print("Array b:", b)

# ================= LOGICAL & COMPARISON FUNCTIONS =================
print("\n===== LOGICAL & COMPARISON FUNCTIONS =====")

# greater than
print("greater():", np.greater(a, b))

# less than
print("less():", np.less(a, b))

# equal
print("equal():", np.equal(a, b))

# not equal
print("not_equal():", np.not_equal(a, b))

# logical_and()
print("logical_and():", np.logical_and(a > 20, a < 50))

# logical_or()
print("logical_or():", np.logical_or(a < 20, a > 40))

# logical_not()
print("logical_not():", np.logical_not(a > 25))

# any()
print("any():", np.any(a > 45))

# all()
print("all():", np.all(a > 5))

# where()
print("where():", np.where(a > 30, a, 0))
import numpy as np
print("\n===== SORTING & SEARCHING FUNCTIONS =====")

arr = np.array([40, 10, 30, 20])

# 9. sort()
print("sort():", np.sort(arr))

# 10. argsort()
print("argsort():", np.argsort(arr))

# 11. lexsort()
x = np.array([2, 1, 3])
y = np.array([3, 2, 1])
print("lexsort():", np.lexsort((x, y)))

# 12. searchsorted()
sorted_arr = np.array([10, 20, 30, 40])
print("searchsorted():", np.searchsorted(sorted_arr, 25))

# 13. partition()
print("partition():", np.partition(arr, 2))

# 14. unique()
arr2 = np.array([1, 2, 2, 3, 4, 4])
print("unique():", np.unique(arr2))
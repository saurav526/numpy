import numpy as np

print("===== INPUT & OUTPUT FUNCTIONS =====")

# save() – Saves a NumPy array to a binary .npy file
a = np.array([10, 20, 30])
np.save("data.npy", a)

# load() – Loads a NumPy array from a .npy file
b = np.load("data.npy")
print("load():", b)

# savetxt() – Saves array data to a text file
np.savetxt("data.txt", a)

# loadtxt() – Loads numerical data from a text file into an array
c = np.loadtxt("data.txt")
print("loadtxt():", c)
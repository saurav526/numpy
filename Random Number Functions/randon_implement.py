import numpy as np
# ================= RANDOM FUNCTIONS =================
print("\n===== RANDOM FUNCTIONS =====")

np.random.seed(5)
print("rand():", np.random.rand(3))
print("randn():", np.random.randn(3))
print("randint():", np.random.randint(1, 10, 5))
print("random():", np.random.random(3))

arr = np.array([10, 20, 30, 40])
print("choice():", np.random.choice(arr, 2))

np.random.shuffle(arr)
print("shuffle():", arr)

print("permutation():", np.random.permutation([1, 2, 3, 4]))
print("uniform():", np.random.uniform(5, 10, 3))
print("normal():", np.random.normal(0, 1, 3))
print("poisson():", np.random.poisson(3, 3))
print("binomial():", np.random.binomial(10, 0.5, 3))



""" 
seed() – Sets a fixed starting point for random number generation.

rand() – Generates random floating-point numbers between 0 and 1.

randn() – Generates random numbers from a normal distribution.

randint() – Generates random integers within a specified range.

random() – Generates random floating-point numbers between 0 and 1.

choice() – Randomly selects elements from a given array.

shuffle() – Randomly rearranges elements of an array in place.

permutation() – Returns a randomly shuffled copy of an array.

uniform() – Generates random numbers within a specified range.

normal() – Generates random numbers from a normal distribution.

poisson() – Generates random numbers from a Poisson distribution.

binomial() – Generates random numbers from a binomial distribution
"""
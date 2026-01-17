import numpy as np
print("\n========= MATHEMATICAL FUNCTIONS =========")

x = np.array([4, 9, 16, 25])
y = np.array([1, 2, 3, 4])

# Arithmetic operations
print("\nadd():", np.add(x, y))
print("subtract():", np.subtract(x, y))
print("multiply():", np.multiply(x, y))
print("divide():", np.divide(x, y))
print("power():", np.power(x, 2))

# Basic math functions
print("\nsqrt():", np.sqrt(x))
print("absolute():", np.abs([-5, -10, 15]))
print("exp():", np.exp(y))
print("log():", np.log(x))
print("log10():", np.log10(x))

# Trigonometric functions
angles = np.array([0, 30, 45, 90])
radians = np.deg2rad(angles)

print("\nsin():", np.sin(radians))
print("cos():", np.cos(radians))
print("tan():", np.tan(radians))

# Rounding functions
z = np.array([2.3, 4.7, 6.1])
print("\nround():", np.round(z))
print("floor():", np.floor(z))
print("ceil():", np.ceil(z))

# Arithmetic Operations

# add() – Adds corresponding elements of two arrays.

# subtract() – Subtracts elements of one array from another.

# multiply() – Multiplies corresponding elements of arrays.

# divide() – Divides elements of one array by another.

# power() – Raises array elements to a specified power.

# Basic Mathematical Functions

# sqrt() – Returns the square root of each array element.

# abs() – Returns the absolute (positive) value of elements.

# exp() – Calculates exponential value (eⁿ) of elements.

# log() – Computes the natural logarithm of elements.

# log10() – Computes the base-10 logarithm of elements.

# Trigonometric Functions

# sin() – Calculates sine of each element (in radians).

# cos() – Calculates cosine of each element (in radians).

# tan() – Calculates tangent of each element (in radians).

# Rounding Functions

# round() – Rounds elements to the nearest integer.

# floor() – Rounds elements down to the nearest integer.

# ceil() – Rounds elements up to the nearest integer.
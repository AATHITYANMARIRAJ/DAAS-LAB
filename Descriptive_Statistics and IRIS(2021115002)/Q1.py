import matplotlib.pyplot as plt
import numpy as np

# Data
mpg = [19, 19, 19, 20, 21, 21, 25, 25, 25, 26, 26, 28, 29, 31, 31, 32, 32, 33, 34, 35, 36, 37, 37, 38, 38, 38, 38, 41, 43, 43]

# Create stem plot
plt.stem(mpg, linefmt='-C0', markerfmt='C0o', basefmt=' ')

# Identify outliers
q1 = np.percentile(mpg, 25)
q3 = np.percentile(mpg, 75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = [x for x in mpg if x < lower_bound or x > upper_bound]
print("Outliers:", outliers)

plt.title('Stem Plot of Miles Per Gallon (MPG)')
plt.xlabel('Index')
plt.ylabel('MPG')
plt.show()

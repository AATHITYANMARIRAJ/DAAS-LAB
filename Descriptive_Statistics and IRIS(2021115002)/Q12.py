import matplotlib.pyplot as plt
import numpy as np

# Data
grades = [77, 78, 76, 81, 86, 51, 79, 82, 84, 99]

# Create stem-and-leaf plot
plt.figure()
plt.stem(grades, linefmt='-C0', markerfmt='C0o', basefmt=' ')

# Identify potential outliers
q1 = np.percentile(grades, 25)
q3 = np.percentile(grades, 75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = [x for x in grades if x < lower_bound or x > upper_bound]
print("Potential outliers:", outliers)

plt.title('Stem-and-Leaf Plot of Chemistry Exam Grades')
plt.xlabel('Index')
plt.ylabel('Grade')
plt.show()

import matplotlib.pyplot as plt

# Data
movies_watched = [0, 5, 1, 9, 2, 6, 3, 4, 4, 1]

# Create box plot
plt.boxplot(movies_watched)

# Add labels and title
plt.title('Box Plot of Number of Movies Watched Previous Week')
plt.xlabel('Number of Movies')
plt.ylabel('Frequency')

# Display the plot
plt.show()

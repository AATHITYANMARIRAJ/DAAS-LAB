import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample Iris dataset
data = """
sepal_length,sepal_width,petal_length,petal_width,species
5.1,3.5,1.4,0.2,setosa
4.9,3.0,1.4,0.2,setosa
4.7,3.2,1.3,0.2,setosa
4.6,3.1,1.5,0.2,setosa
5.0,3.6,1.4,0.2,setosa
5.4,3.9,1.7,0.4,setosa
4.6,3.4,1.4,0.3,setosa
5.0,3.4,1.5,0.2,setosa
4.4,2.9,1.4,0.2,setosa
4.9,3.1,1.5,0.1,setosa
"""

# Convert the data string into a StringIO object and then read it as a DataFrame
from io import StringIO
iris_df = pd.read_csv(StringIO(data))

# Take a sample of 10 entries
sample_df = iris_df.sample(n=10)

# Draw box plot using Seaborn
sns.boxplot(data=sample_df.iloc[:, :-1])  # Exclude the 'species' column
plt.show()

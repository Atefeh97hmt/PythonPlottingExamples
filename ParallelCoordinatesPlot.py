from pandas.plotting import parallel_coordinates
import pandas as pd
import matplotlib.pyplot as plt

# Example data
data = {'Category': ['A', 'B', 'C', 'D'],
        'Feature1': [10, 20, 15, 25],
        'Feature2': [5, 15, 10, 20],
        'Feature3': [8, 18, 13, 23]}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 5))
parallel_coordinates(df, 'Category', colormap='viridis')
plt.title('Parallel Coordinates Plot')
plt.show()

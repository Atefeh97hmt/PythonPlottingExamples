import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(10, 10)

sns.heatmap(data, cmap='viridis')
plt.title('Heatmap')
plt.show()

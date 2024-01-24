import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(100, 2)

sns.violinplot(data=data, palette='Set2')
plt.xlabel('Features')
plt.ylabel('Values')
plt.title('Violin Plot')
plt.show()

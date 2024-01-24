import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(100, 3)

sns.boxplot(data=data)
plt.xlabel('Features')
plt.ylabel('Values')
plt.title('Box Plot')
plt.show()

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(1000)
y = np.random.randn(1000)

sns.jointplot(x=x, y=y, kind='hex', color='blue')
plt.title('Hexbin Plot')
plt.show()

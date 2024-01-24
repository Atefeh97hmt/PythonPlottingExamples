import calmap
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate example data
date_rng = pd.date_range('2024-01-01', '2024-12-31', freq='D')
data = np.random.rand(len(date_rng))

df = pd.DataFrame(data, index=date_rng, columns=['Value'])

# Plot calendar heatmap
calmap.calendarplot(df['Value'], fig_kws={'figsize': (8, 6)}, yearlabel_kws={'color': 'black'})
plt.title('Calendar Heatmap')
plt.show()

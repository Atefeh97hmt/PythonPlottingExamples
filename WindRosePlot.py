import matplotlib.pyplot as plt
from matplotlib.projections import PolarAxes
import numpy as np

# Example wind data
directions = np.arange(0, 360, 45)
speeds = np.random.uniform(0, 10, size=len(directions))

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

ax.set_rlabel_position(0)
ax.set_yticklabels([])

ax.plot(np.radians(directions), speeds, linewidth=2, linestyle='solid', color='b')
ax.fill_between(np.radians(directions), 0, speeds, alpha=0.4, color='b')

plt.title('Wind Rose Plot')
plt.show()

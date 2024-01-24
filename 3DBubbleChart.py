import matplotlib.pyplot as plt
import numpy as np

# Example data
x = np.random.rand(50)
y = np.random.rand(50)
z = np.random.rand(50)
size = np.random.rand(50) * 100

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, s=size, c='skyblue', marker='o', alpha=0.8)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Bubble Chart')
plt.show()

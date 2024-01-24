import matplotlib.pyplot as plt
import pandas as pd

# Generate example data
data = {'Categories': ['Category A', 'Category B', 'Category C', 'Category D', 'Category E'],
        'Values': [30, 20, 15, 10, 25]}
df = pd.DataFrame(data)

df = df.sort_values(by='Values', ascending=False)
df['Cumulative Percentage'] = (df['Values'].cumsum() / df['Values'].sum()) * 100

fig, ax1 = plt.subplots()

ax1.bar(df['Categories'], df['Values'], color='b')
ax1.set_xlabel('Categories')
ax1.set_ylabel('Values', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(df['Categories'], df['Cumulative Percentage'], color='r', marker='o')
ax2.set_ylabel('Cumulative Percentage', color='r')
ax2.tick_params('y', colors='r')

fig.tight_layout()
plt.title('Pareto Chart')
plt.show()

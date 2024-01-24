import plotly.express as px

fig = px.sunburst(names=['Root', 'A', 'B', 'C', 'D', 'Leaf 1', 'Leaf 2', 'Leaf 3'],
                  parents=['', 'Root', 'Root', 'Root', 'Root', 'A', 'A', 'B'],
                  values=[10, 20, 30, 40, 50, 15, 25, 10])

fig.update_layout(title_text="Sunburst Chart")
fig.show()

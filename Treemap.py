import plotly.express as px

data = dict(
    character=['A', 'B', 'C', 'D'],
    parent=['', '', 'A', 'A'],
    value=[10, 15, 5, 20]
)

fig = px.treemap(data, path=['parent', 'character'], values='value')
fig.update_layout(title_text="Treemap")
fig.show()

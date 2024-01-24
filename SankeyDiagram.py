import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color='black', width=0.5),
        label=["Input", "Process 1", "Process 2", "Output"]
    ),
    link=dict(
        source=[0, 0, 1, 1],
        target=[1, 2, 2, 3],
        value=[8, 4, 2, 8]
    )
)])

fig.update_layout(title_text="Sankey Diagram")
fig.show()

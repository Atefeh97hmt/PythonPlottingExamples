import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y=["Stage 1", "Stage 2", "Stage 3", "Stage 4"],
    x=[400, 300, 200, 100],
    textinfo="value+percent initial"
))

fig.update_layout(title_text="Funnel Plot")
fig.show()

import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Barpolar(
    r=[10, 15, 20, 25, 30, 35, 40, 45],
    theta=[0, 45, 90, 135, 180, 225, 270, 315],
    name='Category A',
    marker_color='red'
))

fig.update_layout(title_text='Rose Plot')
fig.show()

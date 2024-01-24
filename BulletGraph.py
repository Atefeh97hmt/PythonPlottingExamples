import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Indicator(
    mode='number+gauge+delta',
    value=220,
    delta={'reference': 200},
    domain={'x': [0.1, 1], 'y': [0.2, 0.9]},
    title={'text': 'Performance'}
))

fig.update_layout(title_text='Bullet Graph')
fig.show()

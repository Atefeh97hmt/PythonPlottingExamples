import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Indicator(
    mode = "gauge+number",
    value = 75,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Speed"},
    gauge = {
        'axis': {'range': [None, 100]},
        'bar': {'color': "darkblue"},
        'steps': [
            {'range': [0, 25], 'color': "lightgray"},
            {'range': [25, 50], 'color': "gray"},
            {'range': [50, 75], 'color': "darkgray"},
            {'range': [75, 100], 'color': "black"}
        ]
    }
))

fig.update_layout(title_text="Gauge Chart")
fig.show()

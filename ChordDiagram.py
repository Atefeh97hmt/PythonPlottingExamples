import plotly.graph_objects as go

fig = go.Figure(data=[go.Choropleth(
    locations=['A', 'B', 'C', 'D'],
    z=[10, 20, 15, 25],
    text=['Category A', 'Category B', 'Category C', 'Category D'],
    colorscale='Viridis',
    autocolorscale=False,
    reversescale=True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_tickprefix='Count ',
    colorbar_title='Category Count',
)])

fig.update_layout(title_text='Chord Diagram')
fig.show()

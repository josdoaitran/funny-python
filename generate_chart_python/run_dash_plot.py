import dash
from dash import dcc,html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

import pandas as pd
import plotly.express as px
app = dash.Dash(__name__)


labels = ["Automated", "Not-Yet"]
TestCase =  [300,20]

fig= px.pie(values=TestCase, labels= labels, title='Test cases report')


fig2 = go.Figure()
years = [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
         2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012]
fig2.add_trace(go.Bar(x=years,
                y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                   350, 430, 474, 526, 488, 537, 500, 439],
                name='Rest of world',
                marker_color='rgb(55, 83, 109)'
                ))
fig2.add_trace(go.Bar(x=years,
                y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                   299, 340, 403, 549, 499],
                name='China',
                marker_color='rgb(26, 118, 255)'
                ))

fig2.update_layout(
    title='US Export of Plastic Scrap',
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='USD (millions)',
        titlefont_size=16,
        tickfont_size=14,
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

df_bar = pd.DataFrame({
   "Feature": ["Feature1", "Feature2"],
   "Automated": [3,2],
    "Not-Yet": [30,12]
})

fig3 = px.bar(df_bar, x="Feature", y="Automated", barmode="group")

app = dash.Dash()
app.layout = html.Div(
    html.Div([
            html.H3('Feature 1'),
            dcc.Graph(id='g1', figure=fig, style={'display': 'inline-block'}),
            dcc.Graph(id='g2', figure=fig2, style={'display': 'inline-block'}),
            html.H3('Feature 2'),
            dcc.Graph(id='g3', figure=fig3, style={'display': 'inline-block'})
    ]),
)

if __name__ == '__main__':
   app.run_server(debug=True)

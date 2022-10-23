from dash import Dash, dcc, html, Input, Output

from libs.generate_chart_lib import GenerateChart

app = Dash(__name__)
app.layout = html.Div([
    html.H1('Test Case coverage: '),
    html.Div([
        dcc.Graph(id='our_graph')
    ], className='nine columns'),
    dcc.Dropdown(
        options=[
            {'label': 'feature1', 'value': 'f1'},
            {'label': 'feature2', 'value': 'f2'},
        ],
        value='MTE'
        , id='demo-dropdown'),
    html.Div(id='dd-output-container')
])


@app.callback(
    Output('our_graph', 'figure'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    if value == 'f1':
        print('data from f1')
        testcase_data = [300, 20]
        chart_percent = GenerateChart.generate_pie_chart(testcase_data)
    else:
        print('data from !f1')
        testcase_data = [600, 620]
        chart_percent = GenerateChart.generate_pie_chart(testcase_data)
    return chart_percent
    # return f'You have selected {value}'


if __name__ == '__main__':
    app.run_server(debug=True)

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from layouts import homeLayout, faqLayout, aboutLayout, totals
import callbacks


app.layout = html.Div([
    html.Table([
            html.Tr([
                html.Td([
                    dcc.Markdown('''**uscovid19tracker.info**''',style = {'font-size':30,}),
                    html.Span('Last Updated: ', style={'font-size':20}),
                    html.Span(totals['data_date'].iloc[0], style={'font-size':20})
                    ]),
                html.Td(style={'width':'35%'}),
                html.Td(
                    dcc.Link('Home',  href='/', style = {'font-size':20}),
                    style={'vertical-align':'top'}
                ),
                html.Td(
                    dcc.Link('FAQ',  href='/faq', style = {'font-size':20}),
                    style={'vertical-align':'top'}
                ),
                html.Td(
                    dcc.Link('About',  href='/about', style = {'font-size':20}),
                    style={'vertical-align':'top'}
                ),
                html.Td(
                    dcc.Markdown('[Buy Me A Coffee :)](https://buymeacoff.ee/XRPHs5J)', style = {'font-size':20}),
                    style={'vertical-align':'top'}
                ),

            ])
        ], style = {
            'width':'100%'
            }
    ),
    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    app.title = 'US COVID-19 Tracker'
    if pathname == '/' or pathname == '/home':
         return homeLayout
    elif pathname == '/faq':
         return faqLayout
    elif pathname == '/about':
        return aboutLayout
    else:
        return '404'


# if __name__ == '__main__':
#    app.run_server(debug=True)
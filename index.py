import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from layouts import homeLayout, faqLayout, aboutLayout
import callbacks


app.layout = html.Div([
    html.Table([
            html.Tr([
                html.Td(
                    html.H1('''
                        UScovid19tracker.io
                    ''',
                    style = {
                        'font-size':30
                    })
                ),
                html.Td([
                    html.Span('''
                    LAST UPDATED: 
                    ''',
                        style = {
                            'font-size':20
                        }),
                    html.Span(callbacks.getTotals()['data_date'].iloc[0],
                        style = {
                            'font-size':18
                        })
                ]),
                html.Td(style={'width':'35%'}),
                html.Td(
                    dcc.Link('Home',  href='/'
                    , style = {'font-size':20})
                ),
                html.Td(
                    dcc.Link('FAQ',  href='/faq'
                    , style = {'font-size':20})
                ),
                html.Td(
                    dcc.Link('About',  href='/about'
                    , style = {'font-size':20})
                ),
                html.Td(
                    dcc.Link('Buy Me A Coffee :)',href='https://buymeacoff.ee/XRPHs5J'
                    , style = {'font-size':20})
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
    if pathname == '/' or pathname == '/home':
         return homeLayout
    elif pathname == '/faq':
         return faqLayout
    elif pathname == '/about':
        return aboutLayout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)
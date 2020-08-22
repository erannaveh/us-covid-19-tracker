import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from layouts import homeLayout, faqLayout, aboutLayout, totals, homeLayoutMobile, newLayout, classesLayout
#from advancedLayout import advancedLayout
import callbacks
from flask import request



app.layout = html.Div([
    html.Table([
            html.Tr([
                html.Td([
                    dcc.Markdown('''**uscovid19tracker.info**''',style = {'font-size':30,}),
                    html.Span('Most Recent Data: ', style={'font-size':20}),
                    html.Span(totals['data_date'].iloc[len(totals['data_date'])-1], style={'font-size':20})
                    ]),
                html.Td(style={'width':'35%'}),
                html.Td(
                    dcc.Link('Home',  href='/', style = {'font-size':20}),
                    style={'vertical-align':'top'}
                ),
                #html.Td(
                #    dcc.Link('Classes',  href='/classes', style = {'font-size':20}),
                #    style={'vertical-align':'top'}
                #),
                html.Td(
                    dcc.Link('What\'s New',  href='/new', style = {'font-size':20}),
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

def isMobile():
    #print(request.user_agent.string)
    #print(request.user_agent.platform)
    #print(request.user_agent.browser)

    return (request.user_agent.platform == 'iphone' or request.user_agent.platform == 'android')

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    layout = 0
    app.title = 'US COVID-19 Tracker'
    if pathname == '/' or pathname == '/home':
        if(isMobile()):
            layout = homeLayoutMobile
        else:
            layout = homeLayout
    elif pathname == '/advanced':
        #layout = advancedLayout
        layout = homeLayout
    elif pathname == '/faq':
        layout = faqLayout
    elif pathname == '/about':
        layout = aboutLayout
    elif pathname == '/new':
        layout = newLayout
    elif pathname == '/classes':
        layout = classesLayout
    else:
        layout = '404'
    return layout

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from graph_functions import statesSQL, countiesSQL, executeSQL, getStatesGraph, getCountiesGraph
from table_functions import statesTableSQL, countiesTableSQL, executeTableSQL, getStatesTable, getCountiesTable, getBuildYourOwnTable, place_value

def getTotals():
    sql = 'select data_date, cases, deaths, cases_diff, deaths_diff, death_rate from vi_totals;'
    df = executeSQL(sql)
    return df

def getStatesList():
    sql = 'select state from vi_states;'
    df = executeSQL(sql)
    return df['state'].tolist()

def getCountiesList():
    sql = 'select state,county from vi_counties;'
    df = executeSQL(sql)
    return (df['state'] + ":" + df['county']).tolist()

state_indicators = getStatesList()
county_indicators = getCountiesList()
nationally_or_state_indicator_options ={
    'States': ['The Nation'],
    'Counties': ['The Nation'] + state_indicators
}
totals = getTotals()
ordering_indicator_options = {
    'States': [('Cases','cases'),('Deaths','deaths'),('New Cases','cases_diff'),('New Deaths','deaths_diff'),('Death Rate','death_rate'),('% Of Total Cases','cases_pct_total'),('% Of Total Deaths','deaths_pct_total')],
    'Counties': [('Cases','cases'),('Deaths','deaths'),('New Cases','cases_diff'),('New Deaths','deaths_diff'),('Death Rate','death_rate'),('% Of State Cases','cases_pct_state'),('% Of State Deaths',('state_pct_total')),
    ('% Of Total Cases','cases_pct_total'),('% Of Total Deaths','deaths_pct_total')]
}

faqLayout = html.Div([
    html.H1('FAQ',
        style = {'width':'100%',
                    'font-size': 40,
                    'text-decoration':'underline'
                }),
    html.Hr(),
    html.H2('What is COVID-19?',
        style = {'width':'100%',
                    'font-size': 20,
                    'text-decoration':'underline'
                }),
    html.P('COVID-19 is a shortening for "Coronavirus Disease-2019," a disease caused by the novel Coronavirus, SARS-nCov-2019. It is a highly infectious upper respiratory disease that was officially declared a pandemic by the World Health Organization on March 11, 2020.'),
    html.H2('Where is my data from? How often is it updated?',
        style = {'width':'100%',
                    'font-size': 20,
                    'text-decoration':'underline'
                }),
    html.Span('I update my data daily from the New York Times covid-19-data github repository. Specific details about the data can be found ',style={'layout':'inline-block'}),
    dcc.Link('here.',href='https://github.com/nytimes/covid-19-data',style={'layout':'inline-block'}),
    html.H2('Where can I get more information?',
        style = {'width':'100%',
                    'font-size': 20,
                    'text-decoration':'underline'
                }),
    html.Span('Refer to the '), 
    dcc.Link('CDC',href='https://www.cdc.gov'),
    html.Span(' and '),
    dcc.Link('WHO',href='https://www.who.int'),
    html.Span(' websites, as well as your own local authorities, to see the best ways to keep you and those around you safe.')
    ])

aboutLayout = html.Div([
     html.H1('About',
        style = {'width':'100%',
                    'font-size': 40,
                    'text-decoration':'underline'
                }),
    html.Hr(),
    html.P('My name is Eran Naveh and I am a college student at UCSB passionate about software development.'),
    html.P('Feel free to leave any feedback and connect on social media!'),
    html.Span([
        dcc.Link('Email', href='mailto:erannaveh@outlook.com'),
        html.Span(' '),
        dcc.Link('LinkedIn', href='https://www.linkedin.com/in/erannaveh'),
        html.Span(' '),
        dcc.Link('Instagram', href='https://www.instagram.com/erannaveh/')
    ]),
       
])

homeLayout = html.Div([   
        html.Table([
            html.Tr([
                html.Td([
                    dcc.Markdown('''
                        US Total Cases:
                    '''),
                    html.H1(
                        place_value(totals['cases'].iloc[0]),
                    )
                ]),
                html.Td([
                    dcc.Markdown('''
                        US Total Deaths:
                    '''),
                    html.H1(place_value(totals['deaths'].iloc[0]))
                ]),
                html.Td([
                    dcc.Markdown('''
                        US New Cases:
                    '''),
                    html.H1(place_value(totals['cases_diff'].iloc[0]))
                ]),
                html.Td([
                    dcc.Markdown('''
                        US New Deaths:
                    '''),
                    html.H1(place_value(totals['deaths_diff'].iloc[0]))
                ]),
                html.Td([
                    dcc.Markdown('''
                        US Death Rate:
                    '''),
                    html.H1(str(float(totals['death_rate'].iloc[0]*100))[0:4]+'%',
                    )
                ]),
            ], style = {'width':'100%'}
        )
        ], style = {'width':'100%',
                    'font-size': 30,
                    'text-decoration':'underline'
                    }
        ),

        html.Table([
            html.Tr([
                html.Td(
                    html.H1('Compare States', 
                        style={
                            'width':'100%',
                            'font-size':25
                    }),
                    style={
                        'width':'50%'
                    }
                ),
                html.Td(
                    html.H1('Compare Counties', 
                        style={
                            'width':'100%',
                            'font-size':25
                    }),
                    style={
                        'width':'50%'
                    }
                )
            ])
        ],style={
            'width':'100%'
        }),

        html.Table([
            html.Tr([
                html.Td(
                    html.Div([
                        dcc.Dropdown(
                            id='states_selected',
                            options=[{'label': i, 'value': i} for i in state_indicators],
                            value='California',
                            multi=True,
                        ),
                        dcc.RadioItems(
                            id='deathsOrCasesStates',
                            options=[{'label': i, 'value': i} for i in ['Cases', 'Deaths']],
                            value='Cases',
                            labelStyle={'display': 'inline-block'}
                        )
                    ])
                ,style={'width':'50%'}),
                html.Td(
                    html.Div([
                        dcc.Dropdown(
                            id='counties_selected',
                            options=[{'label': i, 'value': i} for i in county_indicators],
                            value='California:Santa Barbara',
                            multi=True
                        ),
                        dcc.RadioItems(
                            id='deathsOrCasesCounties',
                            options=[{'label': i, 'value': i} for i in ['Cases', 'Deaths']],
                            value='Cases',
                            labelStyle={'display': 'inline-block'}
                        )
                    ]),
                    style = {'width':'50%'})
            ],style = {'width':'100%'})
        ],style = {'width':'100%'}),
            
    
        html.Table([
            html.Tr([
                html.Td(
                    dcc.Graph(id='states_indicator_graphic',),
                    style = {'width':'50%'}
                ),
                html.Td(
                    dcc.Graph(id='counties_indicator_graphic'),
                    style = {'width':'50%'}
                )
            ],style = {'width':'100%'})
        ],style = {'width':'99%'}),


      html.Table([
            html.Tr([
                html.Td( 
                    dcc.Graph(id='states_indicator_table'),
                ),
                html.Td(
                    dcc.Graph(id='counties_indicator_table'),
                )
            ],style = {'width':'100%'})
        ],
            style = {
                'width':'99%'
            }           
    ),

       # html.Hr(),
        
        html.Div([
            dcc.Markdown('''
            Find Your Data
            ''')
        ], style={
            'font-size': 25
        }),

        html.Table([
            html.Tr([

            html.Td(
                dcc.Markdown('''Top '''),
            ), 
            
        
            html.Td(
                dcc.Input(
                id='num_states_or_counties',
                type='number',
                value = 5
            )
            ),

            html.Td(dcc.Dropdown(
                id='states_or_counties_indicator',
                options=[{'label': i, 'value': i} for i in nationally_or_state_indicator_options.keys()],
                value='States'
            ), style = {'width':'25%'}
            ),

            html.Td(
                dcc.Markdown(''' in ''')
            ),

            html.Td(dcc.Dropdown(
                id='nationally_or_state_indicator',
                value='The Nation'
            ), style = {'width':'30%'}
            ),
            
            html.Td( 
                dcc.Markdown('''by ''')
            ),
            
            html.Td(dcc.Dropdown(
                id='ordering_indicator',
                value='cases'
            ), style = {'width':'20%'}
            )
            ])
        ]
        ),

        
    
        html.Div([
                dcc.Graph(id='build_your_own_table')
            ], style={'width': '100%', 'display': 'inline-block'}),
    ])
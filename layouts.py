import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from graph_functions import statesSQL, countiesSQL, executeSQL, getStatesGraph, getCountiesGraph
from table_functions import statesTableSQL, countiesTableSQL, executeTableSQL, getStatesTable, getCountiesTable, getBuildYourOwnTable, place_value, make_percent, ordering_indicator_options
from callbacks import getTotals, getStatesList, getCountiesList

state_indicators = ['Top 5 States','Pacific','Mountain','West North Central','West South Central',
                    'East North Central','East South Central','New England','Mid Atlantic','South Atlantic']+getStatesList()
county_indicators = ['Top 5 Counties','Big Cities','Bay Area']+getCountiesList()
nationally_or_state_indicator_options ={
    'States': ['The Nation'],
    'Counties': ['The Nation'] + state_indicators
}
totals = getTotals()


faqLayout = html.Div([
    html.H1('FAQ',
        style = {'width':'100%',
                    'font-size': 40,
                    'text-decoration':'underline'
                }),
    html.Hr(),
    html.H2('What is COVID-19?',
        style = {'width':'100%',
                    'font-size': 30,
                    'text-decoration':'underline'
                }),
    html.P('COVID-19 is a shortening for "Coronavirus Disease-2019," a disease caused by the novel Coronavirus, SARS-nCov-2019. It is a highly infectious upper respiratory disease that was officially declared a pandemic by the World Health Organization on March 11, 2020.',style={'font-size':20}),
    html.H2('Where is my data from? How often is it updated?',
        style = {'width':'100%',
                    'font-size': 30,
                    'text-decoration':'underline'
                }),
    dcc.Markdown('''I update my data daily from the New York Times covid-19-data github repository. Specific details about the data can be found [here](https://github.com/nytimes/covid-19-data).''',style={'font-size':20}),
    html.H2('Where can I get more information?',
        style = {'width':'100%',
                    'font-size': 30,
                    'text-decoration':'underline'
                }),
    dcc.Markdown('''
        Refer to the [CDC](https://www.cdc.gov) and [WHO](https://www.who.int) websites, as well as your own local authorities, to see the best ways to keep you and those around you safe.
    ''',style={'font-size':20}),
    ])

aboutLayout = html.Div([
     html.H1('About',
        style = {'width':'100%',
                    'font-size': 40,
                    'text-decoration':'underline'
                }),
    html.Hr(),
    dcc.Markdown('''My name is Eran Naveh and I am a student at UCSB passionate about software development.''',style={'font-size':25}),
    dcc.Markdown('''I'm always updating and improving this site, so feel free to leave any feedback and connect on social media!''',style={'font-size':25}),
    dcc.Markdown('''
        [Email](mailto:erannaveh@outlook.com) [LinkedIn](https://www.linkedin.com/in/erannaveh) [Instagram](https://www.instagram.com/erannaveh/)
    ''', style={'font-size':25}),
       
])
headerSize = 25
dataSize = 20
headerSizeMobile = 35
dataSizeMobile = 30
homeLayout = html.Div([ 
        html.Table([
            html.Tr([
                html.Td(
                    [dcc.Markdown('''US Total Cases''', style={'font-size':headerSize,'text-decoration':'underline'}),
                     html.H1(place_value(totals['cases'].iloc[0]), style={'font-size':dataSize})],style={'text-align':'center'},
                ),
                html.Td(
                    [dcc.Markdown('''US Total Deaths''', style={'font-size':headerSize,'text-decoration':'underline'}),
                     html.H1(place_value(totals['deaths'].iloc[0]), style={'font-size':dataSize})],style={'text-align':'center'},
                ),
                html.Td(
                    [dcc.Markdown('''US New Cases''', style={'font-size':headerSize,'text-decoration':'underline'}),
                     html.H1(place_value(totals['cases_diff'].iloc[0]), style={'font-size':dataSize})],style={'text-align':'center'},
                ),
                html.Td(
                    [dcc.Markdown('''US New Deaths''', style={'font-size':headerSize,'text-decoration':'underline'}),
                     html.H1(place_value(totals['deaths_diff'].iloc[0]), style={'font-size':dataSize})],style={'text-align':'center'},
                ),
                html.Td(
                    [dcc.Markdown('''US Death Rate''', style={'font-size':headerSize,'text-decoration':'underline'}),
                     html.H1(make_percent(totals['death_rate'].iloc[0]), style={'font-size':dataSize})],style={'text-align':'center'},
                ),
                #html.Td(
                 #   [dcc.Markdown('''UPDATED''', style={'font-size':headerSize,'text-decoration':'underline'}),
                  #   html.H1(totals['data_date'].iloc[0], style={'font-size':dataSize})],style={'text-align':'center'},
                #),
            ]),
        ], style={'width':'100%'}),
        html.Table([
            html.Tr([
                html.Td(
                    html.H1('Compare States and Regions', 
                        style={
                            'width':'100%',
                            'font-size':25,
                            'vertical-align':'center'
                    }),
                    style={
                        'width':'50%',
                        'text-align':'center',
                        'vertical-align':'center'
                    }
                ),
                html.Td(
                    html.H1('Compare Counties and Regions', 
                        style={
                            'width':'100%',
                            'font-size':25
                    }),
                    style={
                        'width':'50%',
                        'text-align':'center'
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
                            options=[{'label': i, 'value': i} for i in ['Cases', 'Deaths','New Cases','New Deaths']],
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
                            options=[{'label': i, 'value': i} for i in ['Cases', 'Deaths','New Cases','New Deaths']],
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
                html.Td(dcc.Graph(id='states_indicator_table'),style={'vertical-align':'top','width':'50%'}),
                html.Td(dcc.Graph(id='counties_indicator_table'),style={'vertical-align':'top','width':'50%'})
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
            'font-size': 25,
            'text-align': 'center'
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

homeLayoutMobile = html.Div([
     html.Table([
            html.Tr([
                html.Td(
                    [dcc.Markdown('''US Total Cases''', style={'font-size':headerSizeMobile,'text-decoration':'underline'}),
                     html.H1(place_value(totals['cases'].iloc[0]), style={'font-size':dataSizeMobile})],style={'text-align':'center'},
                ),
                html.Td(
                    [dcc.Markdown('''US Total Deaths''', style={'font-size':headerSizeMobile,'text-decoration':'underline'}),
                     html.H1(place_value(totals['deaths'].iloc[0]), style={'font-size':dataSizeMobile})],style={'text-align':'center'},
                ),
                html.Td(
                    [dcc.Markdown('''US New Cases''', style={'font-size':headerSizeMobile,'text-decoration':'underline'}),
                     html.H1(place_value(totals['cases_diff'].iloc[0]), style={'font-size':dataSizeMobile})],style={'text-align':'center'},
                ),
                html.Td(
                    [dcc.Markdown('''US New Deaths''', style={'font-size':headerSizeMobile,'text-decoration':'underline'}),
                     html.H1(place_value(totals['deaths_diff'].iloc[0]), style={'font-size':dataSizeMobile})],style={'text-align':'center'},
                ),
                html.Td(
                    [dcc.Markdown('''US Death Rate''', style={'font-size':headerSizeMobile,'text-decoration':'underline'}),
                     html.H1(make_percent(totals['death_rate'].iloc[0]), style={'font-size':dataSizeMobile})],style={'text-align':'center'},
                ),
                #html.Td(
                 #   [dcc.Markdown('''UPDATED''', style={'font-size':headerSize,'text-decoration':'underline'}),
                  #   html.H1(totals['data_date'].iloc[0], style={'font-size':dataSize})],style={'text-align':'center'},
                #),
            ]),
        ], style={'width':'100%'}),


        html.Table([
            html.Tr(
                html.Td(
                    html.H1('Compare States and Regions', 
                        style={
                            'width':'100%',
                            'font-size':30,
                            'vertical-align':'center'
                    }),
                    style={
                        'text-align':'center',
                        'vertical-align':'center'
                    }
                ),
            ),
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
                            options=[{'label': i, 'value': i} for i in ['Cases', 'Deaths','New Cases','New Deaths']],
                            value='Cases',
                            labelStyle={'display': 'inline-block'}
                        )
                    ])
                ,style={'width':'50%'}),
            ]),
            html.Tr([
                html.Td(dcc.Graph(id='states_indicator_graphic', config={'staticPlot': True}),style={'vertical-align':'top','width':'50%'})
            ]),
            html.Tr([
                html.Td(dcc.Graph(id='states_indicator_table', config={'staticPlot': True}),style={'vertical-align':'top','width':'50%'})
            ]),
        ], style={'font-size':30}),

         html.Table([
            html.Tr(
                html.Td(
                    html.H1('Compare Counties and Regions', 
                        style={
                            'width':'100%',
                            'font-size':30,
                            'vertical-align':'center'
                    }),
                    style={
                        'text-align':'center',
                        'vertical-align':'center'
                    }
                ),
            ),
            html.Tr([
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
                            options=[{'label': i, 'value': i} for i in ['Cases', 'Deaths','New Cases','New Deaths']],
                            value='Cases',
                            labelStyle={'display': 'inline-block'}
                        )
                    ]),
                    style = {'width':'50%'})
            ]),
            html.Tr([
                html.Td(dcc.Graph(id='counties_indicator_graphic', config={'staticPlot': True}),style={'vertical-align':'top','width':'50%'})
            ]),
            html.Tr([
                html.Td(dcc.Graph(id='counties_indicator_table', config={'staticPlot': True}),style={'vertical-align':'top','width':'50%'})
            ]),
        ], style={'font-size':30}),

         
        html.Div([
            dcc.Markdown('''
            Find Your Data
            ''')
        ], style={
            'font-size': 35,
            'text-align': 'center'
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
                value = 5,
                style={'width':'100%'}
            ),style={'width':'17%'}
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
            ), style = {'width':'28%'}
            )
            ])
        ], style={'font-size':22}
        ),

        
    
        html.Div([
                dcc.Graph(id='build_your_own_table', config={'staticPlot': True})
            ], style={'width': '100%', 'display': 'inline-block'}),

])
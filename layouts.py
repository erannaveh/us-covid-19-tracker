import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from graph_functions import statesSQL, countiesSQL, executeSQL, getStatesGraph, getCountiesGraph
from table_functions import statesTableSQL, countiesTableSQL, executeTableSQL, getStatesTable, getCountiesTable, getBuildYourOwnTable, place_value, make_percent, ordering_indicator_options
from callbacks import getTotals, getStatesList, getCountiesList, getClassesList

state_indicators = ['US Total','Top 5 States','Pacific','Mountain','West North Central','West South Central',
                    'East North Central','East South Central','New England','Mid Atlantic','South Atlantic']+getStatesList()
county_indicators = ['Top 5 Counties','Big Cities','Bay Area']+getCountiesList()
nationally_or_state_indicator_options ={
    'States': ['The Nation'],
    'Counties': ['The Nation'] + state_indicators
}
totals = getTotals()
numRows = len(totals['data_date'])-1

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
    dcc.Markdown('''I update my data daily from the New York Times covid-19-data github repository. Specific details about the data can be found [here](https://github.com/nytimes/covid-19-data). My population data is gathered from the 2018 US census.''',style={'font-size':20}),
    html.H2('Where can I get more information?',
        style = {'width':'100%',
                    'font-size': 30,
                    'text-decoration':'underline'
                }),
    dcc.Markdown('''
        Refer to the [CDC](https://www.cdc.gov) and [WHO](https://www.who.int) websites, as well as your own local authorities, to see the best ways to keep you and those around you safe.
    ''',style={'font-size':20}),
    ])

newLayout = html.Div([
     html.H1('What\'s New',
        style = {'width':'100%',
                    'font-size': 40,
                    'text-decoration':'underline'
                }),
    html.Hr(),
    html.H2('July 10, 2020',
        style = {'width':'100%',
                    'font-size': 30,
                    'text-decoration':'underline'
                }),
    html.P('- Added "Classes" section, allowing users to check which UCSB classes are in-person, online, or hybrid. Intended to help international students find in-person courses and for non-international students to see if they can give up their spot in any courses, due to new ICE regulations.',style={'font-size':20}),
    html.Hr(),
    html.H2('July 8, 2020',
        style = {'width':'100%',
                    'font-size': 30,
                    'text-decoration':'underline'
                }),
    html.P('- Added New Cases Per Capita and New Deaths Per Capita for States, Counties, and US graphs',style={'font-size':20}),
    html.P('- Changed per capita amount for Counties graph from 1k to 100k',style={'font-size':20}),
    html.Hr(),
    html.H2('June 28, 2020',
        style = {'width':'100%',
                    'font-size': 30,
                    'text-decoration':'underline'
                }),
    html.P('- Fixed formatting for build-your-own-table on mobile',style={'font-size':20}),
    html.P('- Added #BLM - CLICK ME button',style={'font-size':20}),
    html.Hr(),
    html.H2('May 20, 2020',
        style = {'width':'100%',
                    'font-size': 30,
                    'text-decoration':'underline'
                }),
    html.P('- Allowed for ascending order in build-your-own-table',style={'font-size':20}),
    html.P('- Aesthetic touches',style={'font-size':20}),
    html.Hr(),
    html.H2('April 19, 2020',
        style = {'width':'100%',
                    'font-size': 30,
                    'text-decoration':'underline'
                }),
    html.P('- Added US Total Data under States Graph',style={'font-size':20}),
    html.P('- Added logarithmic scale',style={'font-size':20}),
    html.P('- Added per capita cases/deaths for both States and Counties',style={'font-size':20}),
    html.P('- Reorganized layout to make these added features easier to use',style={'font-size':20}),
    html.Hr(),
    html.H2('April 12, 2020',
        style = {'width':'100%',
                    'font-size': 30,
                    'text-decoration':'underline'
                }),
    html.P('- Optimized for mobile',style={'font-size':20}),
    html.Hr(),
    html.H2('April 7, 2020',
        style = {'width':'100%',
                    'font-size': 30,
                    'text-decoration':'underline'
                }),
    html.P('- Site launched',style={'font-size':20}),
    ])

aboutLayout = html.Div([
     html.H1('About',
        style = {'width':'100%',
                    'font-size': 40,
                    'text-decoration':'underline'
                }),
    html.Hr(),
    dcc.Markdown('''My name is Eran Naveh and I am a student at the University of California, Santa Barbara, passionate about software development. After launching this site in early April, I devoted my time sheltered in place to learning more about the trends in COVID-19, constantly improving the functionality of my software.''',style={'font-size':25}),
    html.H1('\n'),
    dcc.Markdown('''I'm always looking for ways to update and enhance this site, so please feel free to leave any feedback or connect with me on social media!''',style={'font-size':25}),
    dcc.Markdown('''
        [Email](mailto:erannaveh@outlook.com) [LinkedIn](https://www.linkedin.com/in/erannaveh) [Instagram](https://www.instagram.com/erannaveh/)
    ''', style={'font-size':25}),       
    html.H1('\n'),
    html.H1('\n'),
    html.H1('\n'),
    html.H1('\n'),
    html.Hr(),  
    dcc.Markdown('''
        Read about my website here!
    ''',style={'font-size':30}),
    dcc.Markdown('''
        - [University of California Newsroom](https://www.universityofcalifornia.edu/news/uc-thanks)
        - [University of California Social Media](https://www.facebook.com/universityofcalifornia/posts/10156862587921923)
        - [UCSB Current](https://www.news.ucsb.edu/2020/019859/tracking-spread)
        - [SB Independent](https://www.independent.com/2020/04/18/new-coronavirus-app-compares-country-and-counties/)
    ''',style={'font-size':25}),
    ])

headerSize = 30
dataSize = 25
headerSizeMobile = 35
dataSizeMobile = 30
homeLayout = html.Div([ 

        dcc.ConfirmDialogProvider(
            children=html.Div(html.Button('#BLM - CLICK ME', style={'color':'red','font-size':30,'font-family':'Futura, system-ui'}),style={'text-align':'center','margin-top':'1.2em'}),
            id='popup',
            message='Black Americans and other POC are disproportionately affected by COVID-19 due to a history of systemic racism in healthcare, housing, and city planning, among many other institutions. I will be donating all future proceeds from this website to organizations that help combat racism in America. I urge you to donate, sign petitions, and safely protest. \n\n #BlackLivesMatter'
            ),
        html.Table([
            html.Tr([
                html.Td(
                    [dcc.Markdown('''US Total Cases''', style={'font-size':headerSize,'text-decoration':'underline'}),
                     html.H1(place_value(totals['cases'].iloc[numRows]), style={'font-size':dataSize})],style={'text-align':'center'},
                ),
                html.Td(
                    [dcc.Markdown('''US Total Deaths''', style={'font-size':headerSize,'text-decoration':'underline'}),
                     html.H1(place_value(totals['deaths'].iloc[numRows]), style={'font-size':dataSize})],style={'text-align':'center'},
                ),
                html.Td(
                    [dcc.Markdown('''US New Cases''', style={'font-size':headerSize,'text-decoration':'underline'}),
                     html.H1(place_value(totals['cases_diff'].iloc[numRows]), style={'font-size':dataSize})],style={'text-align':'center'},
                ),
                html.Td(
                    [dcc.Markdown('''US New Deaths''', style={'font-size':headerSize,'text-decoration':'underline'}),
                     html.H1(place_value(totals['deaths_diff'].iloc[numRows]), style={'font-size':dataSize})],style={'text-align':'center'},
                ),
                html.Td(
                    [dcc.Markdown('''US Death Rate''', style={'font-size':headerSize,'text-decoration':'underline'}),
                     html.H1(make_percent(totals['death_rate'].iloc[numRows]), style={'font-size':dataSize})],style={'text-align':'center'},
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
                        html.Div(
                            dcc.Dropdown(
                            id='states_selected',
                            options=[{'label': i, 'value': i} for i in state_indicators],
                            value=['US Total','California'],
                            multi=True,
                            ),style={'float':'left','width':'70%'}
                        ),
                        html.Div(
                            dcc.Dropdown(
                            id='deathsOrCasesStates',
                            options=[{'label': i, 'value': i} for i in ['Cases', 'Deaths','New Cases','New Deaths','Cases/Capita (100k)','Deaths/Capita (100k)', 'New Cases/Capita (100k)','New Deaths/Capita (100k)']],
                            value='Cases',
                            clearable=False
                            ),style={'float':'right','width':'30%','font-size':14}
                        ),
                        dcc.RadioItems(
                            id='linearOrLogStates',
                            options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                            value='Linear',
                            labelStyle={'display': 'inline-block'}
                        )
                    ])
                ,style={'width':'50%'}),
                html.Td(
                    html.Div([
                        html.Div(
                            dcc.Dropdown(
                            id='counties_selected',
                            options=[{'label': i, 'value': i} for i in county_indicators],
                            value='California:Santa Barbara',
                            multi=True,
                            ),style={'float':'left','width':'70%'}
                        ),
                        html.Div(
                            dcc.Dropdown(
                            id='deathsOrCasesCounties',
                            options=[{'label': i, 'value': i} for i in ['Cases', 'Deaths','New Cases','New Deaths','Cases/Capita (100k)','Deaths/Capita (100k)','New Cases/Capita (100k)','New Deaths/Capita (100k)']],
                            value='Cases',
                            clearable=False
                            ),style={'float':'right','width':'30%','font-size':14}
                        ),
                        dcc.RadioItems(
                            id='linearOrLogCounties',
                            options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                            value='Linear',
                            labelStyle={'display': 'inline-block'}
                        )
                    ])
                ,style={'width':'50%'}),
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

            html.Td(dcc.Dropdown(
                id='top_or_bottom',
                options=[{'label': i, 'value': i} for i in ['Top','Bottom']],
                value='Top',
                clearable=False
            ), style = {'width':'10%'}
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
                value='States',
                clearable=False
            ), style = {'width':'25%'}
            ),

            html.Td(
                dcc.Markdown(''' in ''')
            ),

            html.Td(dcc.Dropdown(
                id='nationally_or_state_indicator',
                value='The Nation',
                clearable=False
            ), style = {'width':'30%'}
            ),
            
            html.Td( 
                dcc.Markdown('''by ''')
            ),
            
            html.Td(dcc.Dropdown(
                id='ordering_indicator',
                value='cases',
                clearable=False
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
    dcc.ConfirmDialogProvider(
            children=html.Div(html.Button('#BLM - CLICK ME', style={'color':'red','font-size':30,'font-family':'Futura, system-ui'}),style={'text-align':'center','margin-top':'1.2em'}),
            id='popup',
            message='Black Americans and other POC are disproportionately affected by COVID-19 due to a history of systemic racism in healthcare, housing, and city planning, among many other institutions. I will be donating all future proceeds from this website to organizations that help combat racism in America. I urge you to donate, sign petitions, and safely protest. \n\n #BlackLivesMatter'
            ),
     html.Table([
            html.Tr([
                html.Td(
                    [dcc.Markdown('''US Total Cases''', style={'font-size':headerSizeMobile,'text-decoration':'underline'}),
                     html.H1(place_value(totals['cases'].iloc[numRows]), style={'font-size':dataSizeMobile})],style={'text-align':'center'},
                ),
                html.Td(
                    [dcc.Markdown('''US Total Deaths''', style={'font-size':headerSizeMobile,'text-decoration':'underline'}),
                     html.H1(place_value(totals['deaths'].iloc[numRows]), style={'font-size':dataSizeMobile})],style={'text-align':'center'},
                ),
                html.Td(
                    [dcc.Markdown('''US New Cases''', style={'font-size':headerSizeMobile,'text-decoration':'underline'}),
                     html.H1(place_value(totals['cases_diff'].iloc[numRows]), style={'font-size':dataSizeMobile})],style={'text-align':'center'},
                ),
                html.Td(
                    [dcc.Markdown('''US New Deaths''', style={'font-size':headerSizeMobile,'text-decoration':'underline'}),
                     html.H1(place_value(totals['deaths_diff'].iloc[numRows]), style={'font-size':dataSizeMobile})],style={'text-align':'center'},
                ),
                html.Td(
                    [dcc.Markdown('''US Death Rate''', style={'font-size':headerSizeMobile,'text-decoration':'underline'}),
                     html.H1(make_percent(totals['death_rate'].iloc[numRows]), style={'font-size':dataSizeMobile})],style={'text-align':'center'},
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
                        html.Div(
                            dcc.Dropdown(
                            id='states_selected',
                            options=[{'label': i, 'value': i} for i in state_indicators],
                            value=['US Total','California'],
                            multi=True,
                            ),style={'float':'left','width':'50%'}
                        ),
                        html.Div(
                            dcc.Dropdown(
                            id='deathsOrCasesStates',
                            options=[{'label': i, 'value': i} for i in ['Cases', 'Deaths','New Cases','New Deaths','Cases/Capita (100k)','Deaths/Capita (100k)','New Cases/Capita (100k)','New Deaths/Capita (100k)']],
                            value='Cases',
                            clearable=False
                            ),style={'float':'right','width':'50%'}
                        ),
                    ])
                ,style={'width':'50%'}),
            ]),
            html.Tr( dcc.RadioItems(
                            id='linearOrLogStates',
                            options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                            value='Linear',
                            labelStyle={'display': 'inline-block'}
                        )
            ),
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
                        html.Div(
                            dcc.Dropdown(
                            id='counties_selected',
                            options=[{'label': i, 'value': i} for i in county_indicators],
                            value='California:Santa Barbara',
                            multi=True,
                            ),style={'float':'left','width':'50%'}
                        ),
                        html.Div(
                            dcc.Dropdown(
                            id='deathsOrCasesCounties',
                            options=[{'label': i, 'value': i} for i in ['Cases', 'Deaths','New Cases','New Deaths','Cases/Capita (100k)','Deaths/Capita (100k)','New Cases/Capita (100k)','New Deaths/Capita (100k)']],
                            value='Cases',
                            clearable=False
                            ),style={'float':'right','width':'50%'}
                        ),
                    ])
                ,style={'width':'50%'})
            ]),
            html.Tr(
                dcc.RadioItems(
                            id='linearOrLogCounties',
                            options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                            value='Linear',
                            labelStyle={'display': 'inline-block'}
                        )
            ),
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

            html.Td(dcc.Dropdown(
                id='top_or_bottom',
                options=[{'label': i, 'value': i} for i in ['Top','Bottom']],
                value='Top',
                clearable=False
            ), style = {'width':'14%'}
            ),
            
        
            html.Td(
                dcc.Input(
                id='num_states_or_counties',
                type='number',
                value = 5,
                style={'width':'100%'}
            ),style={'width':'14%'}
            ),

            html.Td(dcc.Dropdown(
                id='states_or_counties_indicator',
                options=[{'label': i, 'value': i} for i in nationally_or_state_indicator_options.keys()],
                value='States',
                clearable=False
            ), style = {'width':'23%'}
            ),

            html.Td(
                dcc.Markdown('''in''')
            ),

            html.Td(dcc.Dropdown(
                id='nationally_or_state_indicator',
                value='The Nation',
                clearable=False
            ), style = {'width':'28%'}
            ),
            
            html.Td( 
                dcc.Markdown('''by''')
            ),
            
            html.Td(dcc.Dropdown(
                id='ordering_indicator',
                value='cases',
                clearable=False
            ), style = {'width':'30%'}
            )
            ])
        ], style={'font-size':20}
        ),

        
    
        html.Div([
                dcc.Graph(id='build_your_own_table', config={'staticPlot': True})
            ], style={'width': '100%', 'display': 'inline-block'}),
    ])

classesLayout = html.Div([
    dcc.ConfirmDialogProvider(
        children=html.Div(html.Button('INFO - CLICK ME', style={'color':'red','font-size':30,'font-family':'Futura, system-ui'}),style={'text-align':'center','margin-top':'1.2em'}),
        id='popup',
        message='This service is meant to help international UCSB students find an in-person or hybrid class so that they can stay in the US. If you are not an international student and you are in an in-person or hybrid class, consider giving your spot to an international student who needs it. \n\nI populate my class data from the UCSB GOLD API, using the guidelines found on the front page of GOLD to determine whether or not a given class is in-person, online, or hybrid. These lists are generated automatically based on these guidelines, so there may be mistakes as administration continues inputting data on classes. Things are constantly changing so please make sure to double check on GOLD and with faculty if you think your class may be in-person. I update my class data every day.'
    ),
    
    html.Hr(),

    html.H1('Find Your Class', 
        style={
            'width':'100%',
            'font-size':30,
            'vertical-align':'center',
            'text-align':'center'
    }),

    html.Hr(),

    html.Table(
        html.Tr([
            html.Td(
                dcc.Dropdown(
                    id='onlineOrInPerson',
                    options=[{'label': i, 'value': i} for i in ['In Person', 'Hybrid','Online']],
                    value='In Person',
                    multi=True,
                    clearable=False
                ),style={'width':'50%'}
            ),
            html.Td(
                dcc.Dropdown(
                    id='undergradOrGrad',
                    options=[{'label': i, 'value': i} for i in ['Undergrad', 'Grad']],
                    value='Undergrad',
                    multi=True,
                    clearable=False
                ),style={'width':'50%'}
            ),
        ]),
        style={'width':'100%'}
    ),
    

    dcc.Dropdown(
        id='course',
        options=[{'label': i, 'value': i} for i in getClassesList('In Person','Undergrad')],
        value='CHEM      6BL',
        multi=False,
        clearable=False
    ),
    html.Hr(),
    html.H1(id='class_title'),
    html.Hr(),
    html.H2(id='class_description'),
    html.Table([
        html.Tr([
            html.Td(id='class_code',style={'white-space':'pre-wrap'}),
            html.Td(id='class_days',style={'white-space':'pre-wrap'}),
            html.Td(id='class_time',style={'white-space':'pre-wrap'}),
        ]),
    ],style={'width':'100%','font-size':20}),

    html.Hr()
])
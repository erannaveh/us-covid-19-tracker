from dash.dependencies import Input, Output
from graph_functions import statesSQL, countiesSQL, executeSQL, getStatesGraph, getCountiesGraph
from table_functions import statesTableSQL, countiesTableSQL, executeTableSQL, getStatesTable, getCountiesTable, getBuildYourOwnTable, place_value
from class_functions import getData
from collections import OrderedDict

from app import app

def getTotals():
    sql = 'select data_date,cases, deaths, cases_diff, deaths_diff, death_rate from us_totals;'
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

onlineOrInPersonSwitcher = {
    'In Person':"'IP'",
    'Hybrid':"'H'",
    'Online': "'OL'"
}

undergradOrGradSwitcher = {
    'Undergrad' : "'U'",
    'Grad' : "'G'"
}

def getClassesList(onlineOrInPerson, undergradOrGrad):
    if not onlineOrInPerson:
        onlineOrInPerson = 'In Person'
    if not undergradOrGrad:
        undergradOrGrad = 'Undergrad'
    if isinstance(onlineOrInPerson,list):
        onlineOrInPerson = ','.join([onlineOrInPersonSwitcher[i] for i in onlineOrInPerson])
    else:
        onlineOrInPerson = onlineOrInPersonSwitcher[onlineOrInPerson]
    if isinstance(undergradOrGrad, list):
        undergradOrGrad = ','.join([undergradOrGradSwitcher[i] for i in undergradOrGrad])
    else:
        undergradOrGrad = undergradOrGradSwitcher[undergradOrGrad]
    
    onlineOrInPerson = '('+onlineOrInPerson+')'
    undergradOrGrad = '('+undergradOrGrad+')'
    sql = 'select enrollCode, courseId from classes where online in '+onlineOrInPerson+' and level in '+undergradOrGrad+';'
    df = executeSQL(sql)
    return (df['courseId']).tolist()

state_indicators = getStatesList()
county_indicators = getCountiesList()
nationally_or_state_indicator_options ={
    'States': ['The Nation'],
    'Counties': ['The Nation'] + state_indicators
}
totals = getTotals()
ordering_indicator_options = {
    'States': [('Cases','cases'),('Deaths','deaths'),('New Cases','cases_diff'),('New Deaths','deaths_diff'),('Death Rate','death_rate'),('% Total Cases','cases_pct_total'),('% Total Deaths','deaths_pct_total')],
    'Counties': [('Cases','cases'),('Deaths','deaths'),('New Cases','cases_diff'),('New Deaths','deaths_diff'),('Death Rate','death_rate'),('% State Cases','cases_pct_state'),('% State Deaths',('deaths_pct_state')),
    ('%  Total Cases','cases_pct_total'),('% Total Deaths','deaths_pct_total')]
}

@app.callback(
    Output('nationally_or_state_indicator','options'),
    [Input('states_or_counties_indicator','value')]
)
def set_nationally_or_state_indicator_options(states_or_counties):
    return [{'label': i, 'value': i} for i in nationally_or_state_indicator_options[states_or_counties]]

@app.callback(
    Output('ordering_indicator','options'),
    [Input('states_or_counties_indicator','value')]
)
def set_ordering_indicator_options(stateOrNationally):
    return [{'label': i[0], 'value': i[1]} for i in ordering_indicator_options[stateOrNationally]]
    
@app.callback(
    [Output('states_indicator_graphic', 'figure'),
     Output('states_indicator_table', 'figure')],
    [Input('states_selected', 'value'),
     Input('deathsOrCasesStates', 'value'),
    Input('linearOrLogStates','value')])
def update_states_graph(states_selected, deathsOrCasesStates, linearOrLog):
    graph = getStatesGraph(states_selected,deathsOrCasesStates, linearOrLog)
    table = getStatesTable(states_selected)
    return graph, table


@app.callback(
    [Output('counties_indicator_graphic', 'figure'),
     Output('counties_indicator_table', 'figure')],
    [Input('counties_selected', 'value'),
     Input('deathsOrCasesCounties', 'value'),
     Input('linearOrLogCounties','value')])
def update_counties_graph(counties_selected, deathsOrCasesCounties,linearOrLog):
    graph = getCountiesGraph(counties_selected, deathsOrCasesCounties, linearOrLog)
    table = getCountiesTable(counties_selected)
    return graph, table

@app.callback(
    Output('build_your_own_table','figure'),
    [Input('top_or_bottom','value'),
    Input('num_states_or_counties','value'),
    Input('states_or_counties_indicator','value'),
    Input('nationally_or_state_indicator','value'),
    Input('ordering_indicator','value')])
def update_build_your_own_table(top_or_bottom, num_states_or_counties, states_or_counties, location, ordering_indicator):
    table = getBuildYourOwnTable(top_or_bottom, num_states_or_counties, states_or_counties, location, ordering_indicator)
    return table

@app.callback(
    Output('adv_selections_list','options'),
    [Input('adv_states_or_counties','value'),
    Input('adv_race','value'),
    Input('adv_gender','value'),
    Input('adv_age_group','value'),
    Input('adv_pct_pop','value'),
    Input('adv_pct','value'),
    Input('adv_pop','value'),
    Input('adv_group_name','value'),
    Input('adv_ordering_indicator','value')])
def update_advanced_selections_list(states_or_counties,race,gender,age_group,pct_pop,pct,pop,group_name, ordering_indicator):
    '''return dcc.Checklist(
                    id = 'adv_selections_list',
                    options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': 'Montréal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SF'},
                    ],

    '''


@app.callback(
    Output('course','options'),
    [Input('onlineOrInPerson','value'),
    Input('undergradOrGrad','value')])
def update_class_list(onlineOrInPerson, undergradOrGrad):
    classes = getClassesList(onlineOrInPerson, undergradOrGrad)
    return [{'label': i, 'value': i} for i in list(OrderedDict.fromkeys(classes)) ]

@app.callback(
    Output('class_title','children'),
    [Input('course','value')])
def update_courseId_title(course):
    courseId_title = getData("'"+course+"'",'courseIdandTitle')
    return courseId_title

@app.callback(
    Output('class_description','children'),
    [Input('course','value')])
def update_description(course):
    description = getData("'"+course+"'",'description')
    return description

@app.callback(
    Output('class_code','children'),
    [Input('course','value')])
def update_enrollCode(course):
    enrollCode = 'Enrollment Code: \n' + getData("'"+course+"'",'enrollCode')
    return enrollCode

@app.callback(
    Output('class_days','children'),
    [Input('course','value')])
def update_days(course):
    days = 'Days: \n' + getData("'"+course+"'",'days')
    return days

@app.callback(
    Output('class_time','children'),
    [Input('course','value')])
def update_time(course):
    time = 'Time: \n' + getData("'"+course+"'",'time')
    return time


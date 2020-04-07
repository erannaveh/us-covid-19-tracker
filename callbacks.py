from dash.dependencies import Input, Output
from graph_functions import statesSQL, countiesSQL, executeSQL, getStatesGraph, getCountiesGraph
from table_functions import statesTableSQL, countiesTableSQL, executeTableSQL, getStatesTable, getCountiesTable, getBuildYourOwnTable, place_value

from app import app

def getTotals():
    sql = 'select data_date,cases, deaths, cases_diff, deaths_diff, death_rate from vi_totals;'
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
    'States': [('Cases','cases'),('Deaths','deaths'),('New Cases','cases_diff'),('New Deaths','deaths_diff'),('Death Rate','death_rate'),('% Total Cases','cases_pct_total'),('% Total Deaths','deaths_pct_total')],
    'Counties': [('Cases','cases'),('Deaths','deaths'),('New Cases','cases_diff'),('New Deaths','deaths_diff'),('Death Rate','death_rate'),('% State Cases','cases_pct_state'),('% State Deaths',('state_pct_total')),
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
     Input('deathsOrCasesStates', 'value')])
def update_states_graph(states_selected, deathsOrCasesStates):
    graph = getStatesGraph(states_selected,deathsOrCasesStates)
    table = getStatesTable(states_selected)
    return graph, table


@app.callback(
    [Output('counties_indicator_graphic', 'figure'),
     Output('counties_indicator_table', 'figure')],
    [Input('counties_selected', 'value'),
     Input('deathsOrCasesCounties', 'value')])
def update_counties_graph(counties_selected, deathsOrCasesCounties):
    graph = getCountiesGraph(counties_selected, deathsOrCasesCounties)
    table = getCountiesTable(counties_selected)
    return graph, table

@app.callback(
    Output('build_your_own_table','figure'),
    [Input('num_states_or_counties','value'),
    Input('states_or_counties_indicator','value'),
    Input('nationally_or_state_indicator','value'),
    Input('ordering_indicator','value')])
def update_build_your_own_table(num_states_or_counties, states_or_counties, location, ordering_indicator):
    table = getBuildYourOwnTable(num_states_or_counties, states_or_counties, location, ordering_indicator)
    return table
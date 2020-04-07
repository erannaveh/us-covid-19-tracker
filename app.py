import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from graph_functions import statesSQL, countiesSQL, executeSQL, getStatesGraph, getCountiesGraph
from table_functions import statesTableSQL, countiesTableSQL, executeTableSQL, getStatesTable, getCountiesTable, getBuildYourOwnTable, place_value

print('****** start')


def getTotals():
    sql = 'select cases, deaths, cases_diff, deaths_diff, death_rate from vi_totals;'
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


#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__)
server = app.server
app.config.suppress_callback_exceptions = True

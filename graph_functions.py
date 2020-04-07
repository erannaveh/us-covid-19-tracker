import pandas as pd 
import pymysql as mysql
import plotly.graph_objects as go
import json 
import os


def getDBConnection():
    dbInfoPath = os.getenv('dbinfo')
    with open(dbInfoPath) as f:
        data = json.load(f)
    db = mysql.connect(
        host=data['host'],
        user=data['user'],
        passwd=data['password'],
        database=data['database'],
    )
    return db



def statesSQL(states):
    sql = "select data_date,state,cases,deaths from states where state in("
    states = states.replace(",", "\',\'")
    sql = sql + "'" + states + "') order by state, data_date;"
    return sql

#returns sql command for counties based on input
def countiesSQL(counties):
    counties = counties.split(',')
    sql = "select data_date,state,county,cases,deaths from counties where "
    for county in counties:
        countyStateList = county.split(':')
        sql += "(state='"+countyStateList[0]+"' and county='"+countyStateList[1]+"') or "
    return sql[0:-4]+" order by state, county, data_date;"

def executeSQL(sql):
    db = getDBConnection()
    cursor = getDBConnection().cursor()
    cursor.execute(sql)
    rs = cursor.fetchall()
    cursor.close()
    db.close()
    #convert data to pandas dataframes
    df = pd.DataFrame(rs)
    df.columns = [i[0] for i in cursor.description]
    return df

def getStatesGraph(states_selected, deathsOrCasesStates):
    if (isinstance(states_selected, list)):
        inputStates = ','.join(states_selected)
        sql = statesSQL(inputStates)
    else:
        sql = statesSQL(states_selected)
        states_selected = [states_selected]
    allStatesDF = executeSQL(sql)
    # print(states_selected)
    fig = go.Figure()
    for state in states_selected:
        # print(state)
        stateDF = allStatesDF[allStatesDF['state'] == state]
        # print(stateDF[deathsOrCases.lower()])
        fig.add_trace(go.Scatter(
            x=stateDF['data_date'],
            y=stateDF[deathsOrCasesStates.lower()],
            mode='lines+markers',
            name=state.title() + ' ' + deathsOrCasesStates.title()
        ))
    fig.update_xaxes(
        tickangle=45,
        showgrid=True, 
        gridwidth=1, 
        gridcolor='whitesmoke',
        zeroline=True, 
        zerolinewidth=1, 
        zerolinecolor='black',
        nticks = 25 )
    fig.update_yaxes(
        showgrid=True, 
        gridwidth=2, 
        gridcolor='whitesmoke',
        zeroline=True, 
        zerolinewidth=2, 
        zerolinecolor='black',
        nticks=4)

    fig.update_layout(
                xaxis_title='Date',
                yaxis_title=deathsOrCasesStates.title(),
                paper_bgcolor='white',
                plot_bgcolor='white',
                font=dict(
                    family="Courier New, monospace",
                    size=12,
                    color="black",
                )
            )
    return fig

def getCountiesGraph(counties_selected, deathsOrCasesCounties):
    if (isinstance(counties_selected, list)):
        inputCounties = ','.join(counties_selected)
        sql = countiesSQL(inputCounties)
    else:
        sql = countiesSQL(counties_selected)
        counties_selected = [counties_selected]
    allCountiesDF = executeSQL(sql)
    fig = go.Figure()
    for stateCounty in counties_selected:
        stateCountyList = stateCounty.split(':')
        state = stateCountyList[0]
        county = stateCountyList[1]
        stateDF = allCountiesDF.loc[allCountiesDF['state'] == state]
        countyDF = stateDF.loc[stateDF['county'] == county]
        fig.add_trace(go.Scatter(
            x=countyDF['data_date'],
            y=countyDF[deathsOrCasesCounties.lower()],
            mode='lines+markers',
            name=county.title() + ', ' + state.title() + ' ' + deathsOrCasesCounties.title()
        ))
    fig.update_xaxes(
        tickangle=45,
        showgrid=True, 
        gridwidth=1, 
        gridcolor='whitesmoke',
        zeroline=True, 
        zerolinewidth=1, 
        zerolinecolor='black',
        nticks = 25)
    fig.update_yaxes(
        showgrid=True, 
        gridwidth=2, 
        gridcolor='whitesmoke',
        zeroline=True, 
        zerolinewidth=2, 
        zerolinecolor='black',
        nticks=4)

    fig.update_layout(
                xaxis_title='Date',
                yaxis_title=deathsOrCasesCounties.title(),
                paper_bgcolor='white',
                plot_bgcolor='white',
                font=dict(
                    family="Courier New, monospace",
                    size=12,
                    color="black",
                )
            )
    return fig
    




""" def getStatesGraph(states_selected, deathsOrCasesStates):
    if (isinstance(states_selected, list)):
        inputStates = ','.join(states_selected)
        sql = statesSQL(inputStates)
    else:
        sql = statesSQL(states_selected)
        states_selected = [states_selected]
    allStatesDF = executeSQL(sql)
    # print(states_selected)
    traces = []
    for state in states_selected:
        # print(state)
        stateDF = allStatesDF[allStatesDF['state'] == state]
        # print(stateDF[deathsOrCases.lower()])
        traces.append(dict(
            x=stateDF['data_date'],
            y=stateDF[deathsOrCasesStates.lower()],
            mode='lines+markers',
            name=state.title() + ' ' + deathsOrCasesStates.title()
        ))
    if (states_selected == None):
        traces = []
    return {
               'data': traces,
               'layout': dict(
                   xaxis=dict(tickformat='%b %d', tickmode='linear', title='Date'),
                   yaxis={
                       'title': deathsOrCasesStates,
                       'type': 'linear'
                   },
                   hovermode='closest'
               )
           }  """
#import matplotlib.pyplot as plt 
import pandas as pd 
#import numpy as np
import plotly.graph_objects as go

class layoutConfig:
    headingColor = 'indianred'
    fill_color='indianred'
    graphFont = dict(
            family="Courier New, monospace",
            size=18,
            color="black"
            )
       
#returns sql command for states based on input
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

def executeSQL(cursor, sql):
    cursor.execute(sql)
    rs = cursor.fetchall()
    #convert data to pandas dataframes
    df = pd.DataFrame(rs)
    df.columns = [i[0] for i in cursor.description]
    return df

def getIsolatedStates(cursor, inputStates):
    #sql query for states
    sql = statesSQL(inputStates)
    statesDF = executeSQL(cursor,sql)
    #isolate desired states
    isolatedStates = []
    for state in inputStates.split(','):
        state1 = statesDF.loc[statesDF['state'] == state]
        isolatedStates.append(state1)
    return isolatedStates

def getIsolatedCounties(cursor, inputCounties):
    #sql query for counties
    sql = countiesSQL(inputCounties)
    countiesDF = executeSQL(cursor, sql)
    #isolate desired counties
    isolatedCounties = []
    for countyState in inputCounties.split(','):
        stateCountyList = countyState.split(':')
        states = countiesDF.loc[countiesDF['state'] == stateCountyList[0]]
        counties = states.loc[states['county']==stateCountyList[1]]
        isolatedCounties.append(counties)
    return isolatedCounties


def plotForStates(isolatedStates, deathsOrCases):
    fig = go.Figure()
    for state in isolatedStates:
        fig.add_trace(go.Scatter(
            x = state['data_date'],
            y = state[deathsOrCases],
            mode = 'lines+markers',
            name = state['state'].iloc[0] + ' ' +deathsOrCases.title()
        ))

    fig.update_layout(title=deathsOrCases.title()+' by State',
                   xaxis_title='Date',
                   yaxis_title=deathsOrCases.title(),
                   font=layoutConfig.graphFont
                   )
    fig.show()

def plotForCounties(isolatedCounties, deathsOrCases):
    fig = go.Figure()
    for county in isolatedCounties:
        fig.add_trace(go.Scatter(
            x = county['data_date'],
            y = county[deathsOrCases],
            mode = 'lines+markers',
            name = county['county'].iloc[0] + ' ' +deathsOrCases.title()
        ))
    fig.update_layout(title=deathsOrCases.title()+' by County',
                   xaxis_title='Date',
                   yaxis_title=deathsOrCases.title(),
                   font=layoutConfig.graphFont
                   )
    fig.show()

def plotAllGraphs(cursor, inputStates, inputCounties):
    isolatedStates = getIsolatedStates(cursor, inputStates)
    isolatedCounties = getIsolatedCounties(cursor, inputCounties)
    plotForStates(isolatedStates,'cases')
    plotForStates(isolatedStates,'deaths')
    plotForCounties(isolatedCounties,'cases')
    plotForCounties(isolatedCounties,'deaths')




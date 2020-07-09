import pandas as pd 
import pymysql as mysql
import plotly.graph_objects as go
from table_functions import getDBConnection, top5StatesList, top5CountiesList, statesSwitcher, countiesSwitcher, family

statesGraphSwitcher = {
    'Cases' : 'cases',
    'Deaths' : 'deaths',
    'New Cases': 'cases_diff',
    'New Deaths': 'deaths_diff',
    'Cases/Capita (100k)': 'cases_per_100k',
    'Deaths/Capita (100k)': 'deaths_per_100k',
    'New Cases/Capita (100k)': 'cases_diff_per_100k',
    'New Deaths/Capita (100k)': 'deaths_diff_per_100k',
}

countiesGraphSwitcher = {
    'Cases' : 'cases',
    'Deaths' : 'deaths',
    'New Cases': 'cases_diff',
    'New Deaths': 'deaths_diff',
    'Cases/Capita (100k)': 'cases_per_1k',
    'Deaths/Capita (100k)': 'deaths_per_1k',
    'New Cases/Capita (100k)': 'cases_diff_per_100k',
    'New Deaths/Capita (100k)': 'deaths_diff_per_100k',
}

def nationalDF():
    sql = 'select data_date,cases,deaths,cases_diff,deaths_diff,cases_per_100k,deaths_per_100k,cases_diff_per_100k,deaths_diff_per_100k from us_totals order by data_date;'
    df = executeSQL(sql)
    return df

def statesSQL(states):
    sql = "select data_date,state,cases,deaths,cases_diff,deaths_diff,cases_per_100k,deaths_per_100k,cases_diff_per_100k,deaths_diff_per_100k from states where state in("
    states = states.replace(",", "\',\'")
    sql = sql + "'" + states + "') order by state, data_date;"
    return sql

#returns sql command for counties based on input
def countiesSQL(counties):
    counties = counties.split(',')
    sql = "select data_date,state,county,cases,deaths,cases_diff,deaths_diff,cases_per_1k,deaths_per_1k,cases_diff_per_100k,deaths_diff_per_100k from counties where "
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



def cleanInput(inputs, states_or_counties):
   return
    
def getStatesGraph(states_selected, deathsOrCasesStates, linearOrLog):
    addNational=False
    column = statesGraphSwitcher[deathsOrCasesStates]
    if(not states_selected):
        states_selected = ['Top 5 States']
    for region in statesSwitcher:
        if(region in states_selected):
            if(region=='US Total'):
                del states_selected[states_selected.index(region)]
                addNational = True
            else:
                states_selected = states_selected + statesSwitcher[region]
                del states_selected[states_selected.index(region)]
    fig = go.Figure()
    if(not states_selected):
        df = nationalDF()
        fig.add_trace(go.Scatter(
            x=df['data_date'],
            y=df[column],
            mode='lines+markers',
            name='US Total'
            ))
    else:
        if (isinstance(states_selected, list)):
            inputStates = ','.join(states_selected)
            sql = statesSQL(inputStates)
        else:
            sql = statesSQL(states_selected)
            states_selected = [states_selected]
        allStatesDF = executeSQL(sql)
        for state in states_selected:
            # print(state)
            stateDF = allStatesDF[allStatesDF['state'] == state]
            # print(stateDF[deathsOrCases.lower()])
            fig.add_trace(go.Scatter(
                x=stateDF['data_date'],
                y=stateDF[column],
                mode='lines+markers',
                name=state.title()
            ))
        if(addNational):
            df = nationalDF()
            fig.add_trace(go.Scatter(
                x=df['data_date'],
                y=df[column],
                mode='lines+markers',
                name='US Total'
                ))
    fig.update_xaxes(
        tickangle=45,
        showgrid=True, 
        gridwidth=1, 
        gridcolor='whitesmoke',
        zeroline=True, 
        zerolinewidth=1, 
        zerolinecolor='black',
        nticks = 15 )
    fig.update_yaxes(
        type=linearOrLog.lower(),
        showgrid=True, 
        gridwidth=2, 
        gridcolor='whitesmoke',
        zeroline=True, 
        zerolinewidth=2, 
        zerolinecolor='black',
        nticks=5)

    fig.update_layout(
                xaxis_title='Date',
                yaxis_title=deathsOrCasesStates.title(),
                paper_bgcolor='white',
                plot_bgcolor='white',
                font=dict(
                    family=family,
                    size=16,
                    color="black",
                )
            )
   
    return fig

def getCountiesGraph(counties_selected, deathsOrCasesCounties,linearOrLog):
    column = countiesGraphSwitcher[deathsOrCasesCounties]
    if(not counties_selected):
        counties_selected = ['Top 5 Counties']
    for region in countiesSwitcher:
        if(region in counties_selected):
            counties_selected = counties_selected + countiesSwitcher[region]
            del counties_selected[counties_selected.index(region)]
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
            y=countyDF[column.lower()],
            mode='lines+markers',
            name=county.title() + ',<br>' + state.title() 
        ))
    fig.update_xaxes(
        tickangle=45,
        showgrid=True, 
        gridwidth=1, 
        gridcolor='whitesmoke',
        zeroline=True, 
        zerolinewidth=1, 
        zerolinecolor='black',
        nticks = 15)
    fig.update_yaxes(
        type=linearOrLog.lower(),
        showgrid=True, 
        gridwidth=2, 
        gridcolor='whitesmoke',
        zeroline=True, 
        zerolinewidth=2, 
        zerolinecolor='black',
        nticks=5)

    fig.update_layout(
                xaxis_title='Date',
                yaxis_title=deathsOrCasesCounties.title(),
                paper_bgcolor='white',
                plot_bgcolor='white',
                font=dict(
                    family=family,
                    size=16,
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
import pandas as pd
import pymysql as mysql
import plotly.graph_objects as go
import numpy as np
import os
import json

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


columnNames = {
    'StatesTableColNames': ['State','Cases','Deaths','New <br>Cases','New <br>Deaths','Death <br>Rate','% Total <br>Cases', '% Total <br>Deaths'],
    'CountiesTableColNames': ['County','Cases','Deaths','New <br>Cases','New <br>Deaths', 'Death <br>Rate','% State <br>Cases',
                    '% State <br>Deaths'],#, '% Total <br>Cases', '% Total <br>Deaths'],
    'BYOStatesTableColNames': ['State','Cases','Deaths','New Cases','New Deaths', 'Death Rate', '% Total Cases', '% Total Deaths'],
    'BYOCountiesTableColNames': ['State','County','Cases','Deaths','New Cases','New Deaths', 'Death Rate','% State Cases',
                    '% State Deaths', '% Total Cases', '% Total Deaths']
}

class layout:
    colorscale = [[0,'indianRed'],[.5,'lightgray'],[1,'whitesmoke']]
    headerColor = 'firebrick'
    cellColor = 'whitesmoke'
    tableFont = dict(
                   family="Courier New, monospace",
                    color="black",
                    size = 15
               )
    headerFont = dict(
                   family="Courier New, monospace",
                    color="white",
                    size = 15
               )
    headerAlignment = 'left'
    cellAlignment = ['left','right']

#returns sql command for states based on input
def statesTableSQL(states):
    sql = "select state,cases,deaths,cases_diff,deaths_diff,death_rate,cases_pct_total,deaths_pct_total from vi_states where state in("
    states = states.replace(",", "\',\'")
    sql = sql + "'" + states + "') order by state, data_date;"
    return sql

def countiesTableSQL(counties):
    counties = counties.split(',')
    #sql = "select county,cases,deaths,cases_diff,deaths_diff,death_rate,cases_pct_state,deaths_pct_state,cases_pct_total,deaths_pct_total from vi_counties where "
    sql = "select county,cases,deaths,cases_diff,deaths_diff,death_rate,cases_pct_state,deaths_pct_state from vi_counties where "
    for county in counties:
        countyStateList = county.split(':')
        sql += "(state='"+countyStateList[0]+"' and county='"+countyStateList[1]+"') or "
    return sql[0:-4]+" order by state, county, data_date;"

def buildYourOwnTableSQL(num_states_or_counties, states_or_counties, location, ordering_indicator):
    whereStatement = ''
    select = ''
    if(states_or_counties == 'States'):
        states_or_counties = 'vi_states'
        select = 'state,cases,deaths,cases_diff,deaths_diff,death_rate,cases_pct_total,deaths_pct_total'
    elif(states_or_counties == 'Counties'):
        states_or_counties = 'vi_counties'
        select = 'state,county,cases,deaths,cases_diff,deaths_diff,death_rate,cases_pct_state,deaths_pct_state,cases_pct_total,deaths_pct_total'
        if(location == 'The Nation'):
            whereStatement = ''
        else:
            whereStatement = "where state='" + location + "'"
    sql = 'select '+str(select)+' from ' + str(states_or_counties) + ' ' + str(whereStatement) + ' order by ' + str(ordering_indicator) + ' desc limit ' + str(num_states_or_counties) + ';'
    print(sql)
    return sql



def executeTableSQL(sql):
    db = getDBConnection()
    cursor = db.cursor()
    cursor.execute(sql)
    rs = cursor.fetchall()
    cursor.close()
    db.close()
    df = pd.DataFrame(rs)
    df.columns = [i[0] for i in cursor.description]
    return df

def cleanNames(df, column):
    namesList = df[column].tolist()
    updatedNamesList = []
    wordCount = 1
    for name in namesList:
        if((name.count(' ')+name.count('-'))>wordCount):
            wordCount = name.count(' ')+name.count('-')
        name = name.replace(' ','<br>').replace('-','-<br>').replace('<br><br>','<br>')
        updatedNamesList.append(name)
    wordCount = wordCount + 1
    df[column] = updatedNamesList
    return [df, wordCount]

def place_value(number):
    if(number == None):
        return
    else:
        return ("{:,}".format(number)) 

def make_percent(number):
    if(number == None):
        return
    else:
        return ("{:.2%}".format(number))

def prepareStatesDF(df):
    df = cleanNames(df, 'State')[0]
    df['Cases']= df['Cases'].apply(place_value)
    df['Deaths']= df['Deaths'].apply(place_value)
    df['New <br>Cases']= df['New <br>Cases'].apply(place_value)
    df['New <br>Deaths']= df['New <br>Deaths'].apply(place_value)
    df['Death <br>Rate']= df['Death <br>Rate'].apply(make_percent)
    df['% Total <br>Cases']= df['% Total <br>Cases'].apply(make_percent)
    df['% Total <br>Deaths']= df['% Total <br>Deaths'].apply(make_percent)
    return df

def prepareCountiesDF(df):
    df = cleanNames(df, 'County')[0]
    df['Cases']= df['Cases'].apply(place_value)
    df['Deaths']= df['Deaths'].apply(place_value)
    df['New <br>Cases']= df['New <br>Cases'].apply(place_value)
    df['New <br>Deaths']= df['New <br>Deaths'].apply(place_value)
    df['Death <br>Rate']= df['Death <br>Rate'].apply(make_percent)
    df['% State <br>Cases']= df['% State <br>Cases'].apply(make_percent)
    df['% State <br>Deaths']= df['% State <br>Deaths'].apply(make_percent)
    #df['% Total <br>Cases']= df['% Total <br>Cases'].apply(make_percent)
    #df['% Total <br>Deaths']= df['% Total <br>Deaths'].apply(make_percent)
    return df

def prepareBYOTableDF(df, states_or_counties):
    df['Cases']= df['Cases'].apply(place_value)
    df['Deaths']= df['Deaths'].apply(place_value)
    df['New Cases']= df['New Cases'].apply(place_value)
    df['New Deaths']= df['New Deaths'].apply(place_value)
    df['Death Rate']= df['Death Rate'].apply(make_percent)
    df['% Total Cases']= df['% Total Cases'].apply(make_percent)
    df['% Total Deaths']= df['% Total Deaths'].apply(make_percent)
    if(states_or_counties == 'Counties'):
        df['% State Cases']= df['% State Cases'].apply(make_percent)
        df['% State Deaths']= df['% State Deaths'].apply(make_percent)
    return df

def getCellValues(df, colName):
    cellValues = []
    for i in columnNames[colName]:
        cellValues.append(df[i])
    return cellValues

def getTable(df, cellValues, wordCount=1, BYO=False, ordering_indicator=''):
    """ headerColors = []
    if(BYO):
        for column in df.columns:
            if(column==ordering_indicator):
                headerColors.append('silver')
            else:
                headerColors.append(layout.headerColor)
    else:
        headerColors = layout.headerColor """
    numRows = df.shape[0]
    fig = go.Figure(
        data=[go.Table(
            columnwidth = 200,
            header = dict(
                fill_color = layout.headerColor,
                values = df.columns,
                align=layout.headerAlignment,
                font = layout.headerFont
            ),
            cells=dict(
                values = cellValues,
                fill_color=layout.cellColor,
                align=layout.cellAlignment,
                font = layout.tableFont,
                height= wordCount * 25
            ))
        ])
    if(BYO==False):
        fig.update_layout(autosize=True, margin=go.layout.Margin(l=0, r=0, b=0, t=0, pad=0,autoexpand=True),height=numRows*95)
    else:
        fig.update_layout(autosize=True, margin=go.layout.Margin(l=0, r=0, b=0, t=0, pad=0,autoexpand=True))
    return fig 

top5States = np.array(executeTableSQL(buildYourOwnTableSQL(5,'States','The Nation','Cases'))['state'])
top5StatesList = top5States.tolist()
statesSwitcher={
    'Top 5 States': top5StatesList,
    'Pacific': ['Washington','Oregon','California','Alaska','Hawaii'],
    'Mountain': ['Idaho','Montana','Wyoming','Utah','Colorado','Nevada','Arizona','New Mexico'],
    'West North Central': ['North Dakota','South Dakota','Minnesota','Iowa','Nebraska','Kansas','Missouri'],
    'West South Central': ['Texas','Oklahoma','Arkansas','Louisiana'],
    'East North Central': ['Wisconsin','Michigan','Illinois','Indiana','Ohio'],
    'East South Central': ['Kentucky','Tennessee','Mississippi','Alabama'],
    'New England': ['Maine','Vermont','New Hampshire','Massachusetts','Connecticut','Rhode Island'],
    'Mid Atlantic': ['New York','Pennsylvania','New Jersey','Maryland','Delaware','District of Columbia'],
    'South Atlantic': ['West Virginia','Virginia','North Carolina','South Carolina','Georgia','Florida']

}
top5Counties = (np.array(executeTableSQL(buildYourOwnTableSQL(5,'Counties','The Nation','Cases'))['state'])+":")+np.array(executeTableSQL(buildYourOwnTableSQL(5,'Counties','The Nation','Cases'))['county'])
top5CountiesList = top5Counties.tolist()
countiesSwitcher={
    'Top 5 Counties': top5CountiesList,
    'Big Cities': ['New York:New York City','California:Los Angeles','Illinois:Cook','District of Columbia:District of Columbia','Texas:Harris'],
    'Bay Area': ['California:Napa','California:Solano',
    'California:Santa Clara','California:San Francisco','California:Contra Costa','California:Alameda',
    'California:San Mateo','California:Sonoma','California:Marin'],
}
def cleanInput(inputs, states_or_counties):
    if(not inputs):
        inputs = ['Top 5 '+states_or_counties]
    if(states_or_counties=='States'):
        switcher = statesSwitcher
    else:
        switcher = countiesSwitcher
    for region in switcher:
        if(region in inputs):
            inputs = inputs + switcher[region]
            del inputs[inputs.index(region)]
    if (isinstance(inputs, list)):
        finalInput = ','.join(inputs)
    else:
        finalInput = inputs
    return finalInput

def getStatesTable(states_selected):
    inputStates = cleanInput(states_selected, 'States')
    sql = statesTableSQL(inputStates)
    allStatesDF = executeTableSQL(sql)
    allStatesDF.columns = columnNames['StatesTableColNames']
    allStatesDF = prepareStatesDF(allStatesDF)
    wordCount = cleanNames(allStatesDF, 'State')[1]
    cellValues = getCellValues(allStatesDF, 'StatesTableColNames')
    fig = getTable(allStatesDF, cellValues, wordCount)
    return fig

def getCountiesTable(counties_selected):
    inputCounties = cleanInput(counties_selected,'Counties')
    sql = countiesTableSQL(inputCounties)
    allCountiesDF = executeTableSQL(sql)
    allCountiesDF.columns = columnNames['CountiesTableColNames']
    prepareCountiesDF(allCountiesDF)
    wordCount = cleanNames(allCountiesDF, 'County')[1]
    cellValues = getCellValues(allCountiesDF, 'CountiesTableColNames')
    fig = getTable(allCountiesDF, cellValues, wordCount)
    return fig

def getBuildYourOwnTable(num_states_or_counties, states_or_counties, location, ordering_indicator):
    if(num_states_or_counties==None or num_states_or_counties<1):
        num_states_or_counties = 1
    if(states_or_counties == 'States'):
        colNames = 'BYOStatesTableColNames'
    elif(states_or_counties == 'Counties'):
        colNames = 'BYOCountiesTableColNames'
    columns = columnNames[colNames]
    sql = buildYourOwnTableSQL(num_states_or_counties, states_or_counties, location, ordering_indicator)
    df = executeTableSQL(sql)
    df.columns = columns
    df = prepareBYOTableDF(df, states_or_counties)
    cellValues = getCellValues(df, colNames)
    fig = getTable(df, cellValues, BYO=True)
    return fig
    

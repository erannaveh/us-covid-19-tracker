import pandas as pd
import plotly.graph_objects as go

#compiling data for stats table
"""
stats:
    - daily case increaseX
    - daily death increase X
    - average case increase
    - average death increase
    - rate of doubling
    - death rate X
    - projections??
    for states only:
        - DISPLAY NAT'L AVERAGES FOR COMPARISON
        - proportion of national cases
        - proportion of national deaths
        - proportion of national cases/deaths compared to proportion of national population
    for counties only:
        - DISPLAY STATE AVERAGES FOR COMPARISON
        - proportion of state cases
        - proportion of state deaths
    
"""

class layoutConfig:
    headerColor = 'indianred'
    cellColor = 'whitesmoke'
    tableFont = dict(
                   family="Courier New, monospace",
                    color="black"
               )
    headerAlignment = ['center','center']
    cellAlignment = ['center','center']
    




################################################
# sql statements
################################################

#returns sql command for states based on input
def statesTableSQL(states):
    sql = "select state,cases,deaths,cases_diff,deaths_diff,death_rate,cases_pct_total,deaths_pct_total from vi_states where state in("
    states = states.replace(",", "\',\'")
    sql = sql + "'" + states + "') order by state, data_date;"
    return sql
    
#returns sql command for counties based on input
def countiesTableSQL(counties):
    counties = counties.split(',')
    sql = "select county,cases,deaths,cases_diff,deaths_diff,death_rate,cases_pct_state,deaths_pct_state,cases_pct_total,deaths_pct_total from vi_counties where "
    for county in counties:
        countyStateList = county.split(':')
        sql += "(state='"+countyStateList[0]+"' and county='"+countyStateList[1]+"') or "
    return sql[0:-4]+" order by state, county, data_date;"

# returns sql command for top n states cases/deaths based on input
def topNstatesTableSQL(numStates, deathsOrCases):
    sql = "select state,cases,deaths,population,cases_diff,deaths_diff,death_rate,cases_pct_total,deaths_pct_total from vi_states order by "+deathsOrCases+" desc limit "+str(numStates)+";"
    return sql

# returns sql command for top n counties cases/deaths per state/nationally based on input
def topNCountiesSQL(numCounties, deathsOrCases, state='empty'):
    if(state == 'empty'):
        sql = "select county,state,cases,deaths,cases_diff,deaths_diff,death_rate,cases_pct_state,deaths_pct_state,cases_pct_total,deaths_pct_total from vi_counties order by "+str(deathsOrCases)+" desc limit "+str(numCounties)+";"
    else:
        sql = "select county,state,cases,deaths,cases_diff,deaths_diff,death_rate,cases_pct_state,deaths_pct_state,cases_pct_total,deaths_pct_total from vi_counties where state='"+state+"' order by "+deathsOrCases+" desc limit "+str(numCounties)+";"
    return sql

################################################
# data frames
################################################

#executes sql command and returns corresponding data frame with columns
def executeTableSQL(cursor, sql):
    cursor.execute(sql)
    rs = cursor.fetchall()
    df = pd.DataFrame(rs)
    df.columns = [i[0] for i in cursor.description]
    return df

#returns dataframe based on states query
def getStateQueryDataFrame(cursor, inputStates):
    #sql query for states
    sql = statesTableSQL(inputStates)
    return executeTableSQL(cursor, sql)

#returns dataframe based on counties query
def getCountyQueryDataFrame(cursor, inputCounties):
    #sql query for counties
    sql = countiesSQL(inputCounties)
    return executeTableSQL(cursor, sql)

# returns dataframe for top n states query
def getTopNStatesDataFrame(cursor, numStates, deathsOrCases):
    sql = topNstatesTableSQL(numStates, deathsOrCases)
    return executeTableSQL(cursor, sql)

#returns dataframe for top n counties query
def getTopNCountiesDataFrame(cursor, numCounties, deathsOrCases, state='empty'):
    sql = topNCountiesSQL(numCounties,deathsOrCases, state)
    return executeTableSQL(cursor,sql)

################################################
# isolate stats for stats tables
################################################

#returns integer value of given state cases/deaths based on input
def getStateData(statesDF, state, deathsOrCases):
    return str(int(statesDF.loc[statesDF['state']==state][deathsOrCases]))

#returns integer value of given county cases/deaths based on input
def getCountiesData(countiesDF, county, deathsOrCases):
    return str(int(countiesDF.loc[countiesDF['county']==county][deathsOrCases]))

#returns integer value of given state cases/deaths difference based on input
def getStatesDiff(statesDF, state, deathsOrCases):
    return str(int(statesDF.loc[statesDF['state']==state][deathsOrCases+"_diff"]))

#returns integer value of given county cases/deaths difference based on input
def getCountiesDiff(countiesDF, county, deathsOrCases):
    return str(int(countiesDF.loc[countiesDF['county']==county][deathsOrCases+"_diff"]))

#returns string value of given state death rate based on input
def getStatesDeathRate(statesDF, state):
    rate = statesDF.loc[statesDF['state']==state]['death_rate']
    return str(float(rate*100))[0:4]+"%"

#returns string value of given county death rate based on input
def getCountyDeathRate(countiesDF, county):
    rate = countiesDF.loc[countiesDF['county']==county]['death_rate']
    return str(float(rate*100))[0:4]+"%"

#returns string value of given state % of total cases/deaths based on input
def getStatesPercentOfTotal(statesDF, state, deathsOrCases):
    pct = statesDF.loc[statesDF['state']==state][deathsOrCases+'_pct_total']
    return str(float(pct*100))[0:4]+"%"

#returns string value of given county % of total/state cases/deaths based on input
def getCountiesPercentOf(countiesDF, county, deathsOrCases, stateOrTotal):
    pct = countiesDF.loc[countiesDF['county']==county][deathsOrCases+'_pct_'+stateOrTotal]
    return str(float(pct*100))[0:4]+'%'

################################################
# prepare data frames for table plotting
################################################

#prepares and returns dataframe of ^ data points for states to plot
def createDataFrameStates(cursor, inputStates):
    statesDF = getStateQueryDataFrame(cursor,inputStates)
    inputStatesNew = inputStates.split(',')
    totalRows = []
    for state in inputStatesNew:
        stateRow = [
            state,
            getStateData(statesDF, state, 'cases'),
            getStateData(statesDF, state, 'deaths'),
            getStatesDiff(statesDF, state, 'cases'),
            getStatesDiff(statesDF, state, 'deaths'),
            getStatesDeathRate(statesDF, state),
            getStatesPercentOfTotal(statesDF, state, 'cases'),
            getStatesPercentOfTotal(statesDF,state, 'deaths')
        ]
        totalRows.append(stateRow)
    return pd.DataFrame(totalRows, columns=['State','Cases','Deaths','LastDayCaseIncrease','LastDayDeathIncrease','DeathRate','PercentOfTotalCases','PercentOfTotalDeaths'])

#prepares and returns dataframe of ^ data points for counties to plot
def createDataFrameCounties(cursor,inputCounties):
    countiesDF = getCountyQueryDataFrame(cursor, inputCounties)
    inputCountiesNew = inputCounties.split(',')
    counties = []
    for item in inputCountiesNew:
        counties.append(item[item.find(':')+1:])
    totalRows = []
    for county in counties:
        countyRow = [
            county,
            getCountiesData(countiesDF, county, 'cases'),
            getCountiesData(countiesDF, county, 'deaths'),
            getCountiesDiff(countiesDF, county,'cases'),
            getCountiesDiff(countiesDF, county, 'deaths'),
            getCountyDeathRate(countiesDF, county),
            getCountiesPercentOf(countiesDF, county, 'cases', 'state'),
            getCountiesPercentOf(countiesDF, county, 'deaths', 'state'),
            getCountiesPercentOf(countiesDF, county, 'cases', 'total'),
            getCountiesPercentOf(countiesDF, county, 'deaths', 'total'),
        ]
        totalRows.append(countyRow)
    return pd.DataFrame(totalRows, columns=['County','Cases','Deaths','LastDayCaseIncrease','LastDayDeathIncrease','DeathRate','PercentOfStateCases','PercentOfStateDeaths','PercentOfTotalCases','PercentOfTotalDeaths'])

#prepares and returns dataframe of top n states to be put in table
def createDataFrameTopNStates(cursor, numStates, deathsOrCases):
    df = getTopNStatesDataFrame(cursor, numStates,deathsOrCases)
    df['death_rate'] = df['death_rate'].apply(lambda x: (str(x*100))[0:4]+"%")
    df['cases_pct_total'] = df['cases_pct_total'].apply(lambda x: (str(x*100))[0:4]+"%")
    df['deaths_pct_total'] = df['deaths_pct_total'].apply(lambda x: (str(x*100))[0:4]+"%")
    return df

#prepares and returns dataframe of top n counties to be put in table
def createDataFrameTopNCounties(cursor, numCounties, deathsOrCases, state='empty'):
    df = getTopNCountiesDataFrame(cursor,numCounties,deathsOrCases,state)
    df['death_rate'] = df['death_rate'].apply(lambda x: (str(x*100))[0:4]+"%")
    df['cases_pct_state'] = df['cases_pct_state'].apply(lambda x: (str(x*100))[0:4]+"%")
    df['deaths_pct_state'] = df['deaths_pct_state'].apply(lambda x: (str(x*100))[0:4]+"%")
    df['cases_pct_total'] = df['cases_pct_total'].apply(lambda x: (str(x*100))[0:4]+"%")
    df['deaths_pct_total'] = df['deaths_pct_total'].apply(lambda x: (str(x*100))[0:4]+"%")
    return df

################################################
# plot tables
################################################

def getTable(headerValues, cellValues, title):
    fig = go.Figure(data=[go.Table(
    header=dict(values=headerValues,
                fill_color=layoutConfig.headerColor,
                align=layoutConfig.headerAlignment,
                font = layoutConfig.tableFont
                ),
    cells=dict(values=cellValues,
               fill_color=layoutConfig.cellColor,
               align=layoutConfig.cellAlignment,
               font = layoutConfig.tableFont
               ))
    ])

    fig.update_layout(
        title_text = title,
        font = layoutConfig.tableFont
    )

    fig.show()

#creates and plots table of states data based on input states
def getStatesTable(cursor, inputStates):
    df = createDataFrameStates(cursor, inputStates)
    headerValues = ['State','Cases','Deaths','New Cases','New Deaths','Death Rate','% Of Total Cases','% Of Total Deaths']
    cellValues = [df.State, df.Cases, df.Deaths, df.LastDayCaseIncrease, df.LastDayDeathIncrease, df.DeathRate, df.PercentOfTotalCases, df.PercentOfTotalDeaths]
    title = 'Selected States Statistics'
    getTable(headerValues,cellValues, title)

#creates and plots table of counties data based on input counties
def getCountiesTable(cursor, inputCounties):
    df = createDataFrameCounties(cursor, inputCounties)
    headerValues = ['County','Cases','Deaths','New Cases','New Deaths','Death Rate','% Of State Cases','% Of State Deaths','% Of Total Cases','% Of Total Deaths']
    cellValues = [df.County, df.Cases, df.Deaths, df.LastDayCaseIncrease, df.LastDayDeathIncrease, df.DeathRate, df.PercentOfStateCases, df.PercentOfStateDeaths, df.PercentOfTotalCases, df.PercentOfTotalDeaths]
    title = 'Selected Counties Statistics'
    getTable(headerValues,cellValues, title)

#creates and plots table of top N States based on input
def getTopNStatesTable(cursor, numStates, deathsOrCases):
    if(numStates>54):
        numStates == 54
    elif(numStates<1):
        numStates = 5
    df = createDataFrameTopNStates(cursor, numStates, deathsOrCases)
    headerValues = ['State','Cases','Deaths','Population','New Cases','New Deaths','Death Rate','% Of Total Cases','% Of Total Deaths']
    cellValues = [df.state,df.cases,df.deaths,df.population,df.cases_diff,df.deaths_diff,df.death_rate,df.cases_pct_total,df.deaths_pct_total]
    title = 'Top ' + str(numStates) + ' States By ' + str(deathsOrCases).title()
    getTable(headerValues,cellValues, title)

#creates and plots table of top N counties based on input
def getTopNCountiesTable(cursor, numCounties, deathsOrCases, state='empty'):
    if(numCounties>20):
        numCounties == 20
    elif(numCounties<1):
        numCounties = 5
    df = createDataFrameTopNCounties(cursor, numCounties, deathsOrCases, state)
    
    if(state == 'empty'):
        headerValues = ['County','State','Cases','Deaths','New Cases','New Deaths','Death Rate','% Of State Cases','% Of State Deaths','% Of Total Cases','% Of Total Deaths']
        cellValues = [df.county, df. state,  df.cases, df.deaths, df.cases_diff, df.deaths_diff, df.death_rate, df.cases_pct_state, df.deaths_pct_state, df.cases_pct_total, df.deaths_pct_total]
        title = 'Top ' + str(numCounties) + ' Counties Nationally By ' + str(deathsOrCases).title()
    else:
        headerValues = ['County','Cases','Deaths','New Cases','New Deaths','Death Rate','% Of State Cases','% Of State Deaths','% Of Total Cases','% Of Total Deaths']
        cellValues = [df.county, df.cases, df.deaths, df.cases_diff, df.deaths_diff, df.death_rate, df.cases_pct_state, df.deaths_pct_state, df.cases_pct_total, df.deaths_pct_total]
        title = 'Top ' + str(numCounties) + ' Counties in '+ str(state).title() + ' By ' + str(deathsOrCases).title()
    getTable(headerValues,cellValues, title)

def getAllTables(cursor, inputStates, inputCounties):
    getStatesTable(cursor, inputStates)
    getCountiesTable(cursor,inputCounties)
    getTopNStatesTable(cursor,20, 'cases')
    getTopNStatesTable(cursor,10, 'deaths')
    getTopNCountiesTable(cursor,10,'cases')
    getTopNCountiesTable(cursor,10,'deaths')
    getTopNCountiesTable(cursor,10,'cases', 'California')
    getTopNCountiesTable(cursor,10,'deaths', 'California')

def test(cursor, inputStates, inputCounties):
    """ print('California daily death increase: ',getStatesDiff(cursor, inputStates, 'California', 'deaths'))
    print('Santa Clara daily case increase: ', getCountiesDiff(cursor, inputCounties,'Santa Clara','cases'))
    print('California death rate: ', getStatesDeathRate(cursor, inputStates,'California'))
    print('Santa Clara County death rate: ',getCountyDeathRate(cursor, inputCounties,'Santa Clara'))
    print('California percent of total cases: ', getStatesPercentOfTotal(cursor,inputStates,'California','cases'))
    print('California percent of total deaths: ', getStatesPercentOfTotal(cursor,inputStates,'California','deaths'))
    print('Santa Clara percent of CA cases: ', getCountiesPercentOf(cursor, inputCounties, 'Santa Clara', 'cases','state'))
    print('Santa Clara percent of CA deaths: ', getCountiesPercentOf(cursor, inputCounties, 'Santa Clara', 'deaths','state'))
    print('Santa Clara percent of total cases: ', getCountiesPercentOf(cursor, inputCounties, 'Santa Clara', 'cases','total'))
    print('Santa Clara percent of total deaths: ', getCountiesPercentOf(cursor, inputCounties, 'Santa Clara', 'deaths','total')) """
    getTopNStatesTable(cursor, 5,'deaths')
    getTopNCountiesTable(cursor,5,'deaths')
    getTopNCountiesTable(cursor,5,'cases','New York')


    

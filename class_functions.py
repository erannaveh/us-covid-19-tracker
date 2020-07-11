from table_functions import getDBConnection
import pandas as pd

def executeSQL(sql,columns):
    db = getDBConnection()
    cursor = getDBConnection().cursor()
    cursor.execute(sql)
    rs = cursor.fetchall()
    cursor.close()
    db.close()
    #convert data to pandas dataframes
    df = pd.DataFrame(rs)
    df.columns = columns
    return df

def getCourseIdandTitle(course):
    sql = 'select courseId,courseName from classes where courseId='+course+';'
    df = executeSQL(sql, ['courseId','courseName'])
    return (df['courseId'] + ' - ' + df['courseName'])[0]

def getDescription(course):
    sql = 'select description from classes where courseId='+course+';'
    df = executeSQL(sql,['description'])
    return (df['description'])[0]

def getDays(course):
    sql = 'select days from classes where courseId='+course+';'
    df = executeSQL(sql, ['days'])
    return '\n '.join(df['days'].tolist())


def getTime(course):
    sql = 'select time from classes where courseId='+course+';'
    df = executeSQL(sql, ['time'])
    return '\n '.join(df['time'].tolist())

    
def getEnrollCode(course):
    sql = 'select enrollCode from classes where courseId='+course+';'
    df = executeSQL(sql, ['enrollCode'])
    return '\n '.join(df['enrollCode'].tolist())

    




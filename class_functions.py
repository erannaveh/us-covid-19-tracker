from table_functions import getDBConnection
from graph_functions import executeSQL
import pandas as pd

def getData(course, col):
    sql = 'select enrollCode, courseId, courseName, description, days, time from classes where courseId='+course+';'
    df = executeSQL(sql)
    if col=='courseIdandTitle':
        return (df['courseId'] + ' - ' + df['courseName'])[0]
    elif col=='description':
        return (df['description'])[0]
    else:
        return '\n'.join(df[col].tolist())
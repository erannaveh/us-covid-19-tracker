import sys
import pymysql as mysql
#from createGraphs import *
from createData import *

#connect to db and establish cursor
pwd = sys.argv[1]
db = mysql.connect(
    host = "covid.cng0ove8fvph.us-east-1.rds.amazonaws.com",
    user = "eran",
    passwd = pwd,
    database = "covid",
)
cursor = db.cursor()

"""
input arguments:
    1 - db password
    2 - list of states in format "State1,State2,State3,..."
    3 - list of counties in format "State1:County1,State2:County2,..."
"""
#inputStates = str(sys.argv[2])
#inputCounties = str(sys.argv[3])


inputStates = "California,Washington,New York,New Jersey"
inputCounties = "California:Santa Clara,California:Santa Barbara,California:Los Angeles,New York:New York City"

#plotAllGraphs(cursor, inputStates, inputCounties)
#getAllTables(cursor,inputStates,inputCounties)
#test(cursor, inputStates, inputCounties)

print(executeTableSQL(cursor,statesTableSQL(inputStates)))
"""
API List:
    1. Graph Selected States By Cases/Deaths
    2. Graph Selected Counties By Cases/Deaths
    3. Top N States By Cases/Death
    4. Top N Counties Nationally/State By Cases/Death
    5. Table for Selected States
    6. Table for Selected Counties
"""

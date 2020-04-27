"""
3 script arguments:
    password
    table name
    input file

connect to db with <arg-password>
delete from <arg-table>
read first line from file <arg-inputfile>
prepend data_ to first line (i.e. data_date) 
use first line variable to build sql prefix - 
    insert into <arg-tablename> (<first line variable>) values
    i.e. :
    insert into states(data_date, state, fips, cases, deaths) values (current_date(), 'california', 1,1,1);
for lines 2 to end
    split with ,
    add single quote before and after each value
    concat  values with comma separators
    create full sql and execute
    

argv = ["loadCSV.py",password,"path/us-states.csv","path/us-counties.csv"]
"""
#mysql -h covid.cng0ove8fvph.us-east-1.rds.amazonaws.com -u eran -p
import sys
## import mysql.connector as mysql
import pymysql as mysql
import getpass as gp
import datetime
if (len(sys.argv) < 3):
    print ("\n")
    print ("Insufficent arguments, aborting")
    print ("Please provide: states data file, counties data file [, rows to process]")
    print ("\n")
    exit()

#pwd = sys.argv[1]
pwd = gp.getpass(prompt="Password: ").strip()
while(len(pwd)<5):
    pwd = gp.getpass(prompt="Password (minimum 5 char): ").strip()
statesFilePath = sys.argv[1]
countiesFilePath = sys.argv[2]
if (len(sys.argv)>3):
    rowCount = int(sys.argv[3])
else:
    rowCount = -1

db = mysql.connect(
    host = "covid.cng0ove8fvph.us-east-1.rds.amazonaws.com",
    user = "eran",
    passwd = pwd,
    database = "covid",
)

cursor = db.cursor()

def getTableInfo(tableName):
    if (tableName == "states"):
        colNames = "data_date, state, fips, cases, deaths"
        colValues = "%s, %s, %s, %s, %s"
    if (tableName == "counties"):    
        colNames = "data_date, county, state, fips, cases, deaths"
        colValues = "%s, %s, %s, %s, %s, %s"

    sql = "insert into " + tableName + " (" + colNames + ") values (" + colValues + ");"
    return sql

def loadTable(tableName, filePath, rowCount):
    rl = 0
    rlt = 0
    sql = "delete from " + tableName + ";"
    print(datetime.datetime.now(), " start processing ", tableName, " from ", filePath)
    cursor.execute(sql)
    print(datetime.datetime.now(), " ", cursor.rowcount, " records deleted from ", tableName)
    sql = getTableInfo(tableName)
    with open(filePath) as f:
        next(f)
        for row in f:
            rlt = rlt + 1
            # print (row)
            dataArray = row.split(',')
            try:
                cursor.execute(sql, dataArray)
                rl = rl + 1
            except:
                print (datetime.datetime.now(), " Error executing command for row ", rlt, ", data: ", row)

            rowCount = rowCount - 1
            if (rowCount == 0):
                break
    db.commit()
    print(datetime.datetime.now(), " ", rlt, " lines read from file, ", rl, " rows inserted inserted into ", tableName)

rc = rowCount
loadTable("states", statesFilePath, rc)
rc = rowCount
loadTable("counties", countiesFilePath, rc)








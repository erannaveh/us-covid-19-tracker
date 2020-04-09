#! /bin/bash
# download latest
wget --no-check-certificate https://github.com/nytimes/covid-19-data/archive/master.zip

# unzip latest
unzip -o -j master.zip -d covid-19-data/
python3 loadcsv.py $1 ./covid-19-data/us-states.csv ./covid-19-data/us-counties.csv

mysql -h covid.cng0ove8fvph.us-east-1.rds.amazonaws.com -u admin -p < update-states.sql
mysql -h covid.cng0ove8fvph.us-east-1.rds.amazonaws.com -u admin -p < update-counties.sql

# save file
today="$( date +"%Y%m%d-%H%M%S" )"
mv master.zip master-$today.zip

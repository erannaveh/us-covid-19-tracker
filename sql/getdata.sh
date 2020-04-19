#! /bin/bash

if [[ $1 == '' ]]
then

    echo
    echo ERROR
    echo ERROR Database password missing, please provide a database password
    echo ERROR
    exit 1
fi

if [[ $2 == '' ]]
then

    echo
    echo ERROR
    echo ERROR Database URL missing, please provide a database URL
    echo ERROR
    exit 1
fi

today="$( date +"%Y%m%d-%H%M%S" )"
echo
echo [$today] Start COVID data update
echo
# download latest
wget --no-check-certificate https://github.com/nytimes/covid-19-data/archive/master.zip

# calcualte last download checksum
ck1=$(cksum master.zip | cut -d ' ' -f1)

# get previously downloaded file and its checksum
prevdl=$(ls -tr master-2020* | tail -n1)
ck2=$(cksum $prevdl |cut -d ' ' -f1)

# compare downloads, abort if same
echo New download cksum......- $ck1
echo Previous download file..- $prevdl
echo Previous download cksum.- $ck2
echo

if [[ $ck1 == $ck2 ]]
then
    echo Data not changed, no need to load into database
    echo
    rm -f master.zip
    exit 0
fi

echo New data available, loading into databasse
echo
## unzip latest and load
unzip -o -j master.zip -d covid-19-data/
python3 loadcsv.py $1 ./covid-19-data/us-states.csv ./covid-19-data/us-counties.csv

## update tables for daily delta values
echo Updating states table with daily delta values
echo
mysql -h $2 -u admin -p < update-states.sql
echo Updating counties tables with daily delta values
echo
mysql -h $2 -u admin -p < update-counties.sql

## load and update totals
echo "use covid;" > us.sql;echo "delete from us_totals;" >> us.sql; echo "insert into us_totals(data_date, cases, deaths) values" >> us.sql ; grep -v -i date ./covid-19-data/us.csv | sed  "s/2020/(\"2020/"  | sed "s/,/\",/" | sed "/(/ s/$/),/" >> us.sql ; sed '$s/,$//' us.sql  > us.sql1 ; cp us.sql1 us.sql ; echo ";" >> us.sql
mysql -h $2 -u admin -p < us.sql
mysql -h $2 -u admin -p < update-us.sql


# save file
today="$( date +"%Y%m%d-%H%M%S" )"
echo Renaming data file to master-$today.zip
mv master.zip master-$today.zip
echo
echo Data update complete
echo

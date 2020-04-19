#! /bin/bash
# download latest code
wget --no-check-certificate https://github.com/erannaveh/us-covid-19-tracker/archive/master.zip

# unzip latest
unzip -o master.zip

# save file with date and time
today="$( date +"%Y%m%d-%H%M%S" )"
mv master.zip master-$today.zip



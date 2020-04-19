#!/bin/bash
##procid=$(ps -ef | grep -i app-run | grep -i python3 | cut -d ' ' -f2)
procid=$(pgrep python3)

echo
echo Killing current instance with id $procid
dt=`date '+%Y-%m-%d %H:%M:%S'`
echo $dt Terminated previous server instance with procid $procid >> ./logs/server.log
kill -n 9 $procid

echo
echo cache content before delete
echo
ls -la ./us-covid-19-tracker-master/__pycache__/* | echo $(wc -l) files to be deleted from cache
rm -f ./us-covid-19-tracker-master/__pycache__/*
echo
echo cache content after delete
echo
ls -la ./us-covid-19-tracker-master/__pycache__/* | echo $(wc -l) files in cache after delete


echo starting new instance
echo
cd ./us-covid-19-tracker-master

rm -f __pycache__/*

## to run w/o cache, add -B to the command below (python3 -B)
nohup python3 app-run.py &

## procid=$(ps -ef | grep -i app-run | grep -i python3 | cut -d ' ' -f2)
procid=$(pgrep python3)
echo
echo New process running with id $procid
cd ../
dt=`date '+%Y-%m-%d %H:%M:%S'`
echo $dt Starting new server nstance with procid $procid >> ./logs/server.log



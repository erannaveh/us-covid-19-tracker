#!/bin/bash
## procid=$(ps -ef | grep -i app-run | grep -i python3 | cut -d ' ' -f2)


echo
procid=$(pgrep python3)
SERVICE="python3"
if pgrep -x "$SERVICE" >/dev/null
then
    echo "$SERVICE is running " $procid
else
    echo "$SERVICE is not running"
fi
echo

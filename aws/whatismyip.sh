#!/bin/bash

myip=$(curl -s ifconfig.me)
myip="${myip//\./-}"
echo
echo this is ec2-$myip.compute-1.amazonaws.com [host 1]
echo

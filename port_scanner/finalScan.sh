#!/bin/bash

echo "Running Final Scan..."

cat full_scan.nmap | grep open | cut -d' ' -f1 | cut -d/ -f1 > ports.list
mkdir nmap
nmap -sVC -T5 -Pn -oN nmap/final_scan -p`tr '\n' ',' < ports.list` `cat ip.txt` 

echo "Sleeping...."
sleep 5
echo "Done Sleeping"

echo "Moving files to 'nmap/' directory"
mv full_scan.nmap init_scan.nmap  nmap

ls
echo "Cleaning..."
rm full_scan.*
rm init_scan.*

echo "Cleaned up"
echo "All process done."




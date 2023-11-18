#!/usr/bin/python3

import requests
import os
import subprocess
import threading


# STARTING PORT SCAN SECTION


# This function is to scan 
# all ports at the target ip.
def full_scan(IP):
    print("Running full scan...")
    subprocess.run(["nmap", "-p-", "-oA", 
                    "full_scan", "-Pn", "-T5", 
                    IP])
    print("Done full scan")


# Func to scan on well known ports to get quick result
def init_scan(IP):
    print("Running init scan...")
    subprocess.run(["nmap", "-sVC", "-T5", "-p22,21,80,8080", 
                    "-oA", "init_scan", IP])

    print("Done init scan")


# Check if ip addr file exist or not and create one if not.
if "ip.txt" in os.listdir():
    print("Checking for 'ip.txt' file...")
    print("File found.")
    
    # Check if ip file is empty or not. 
    # If empty it will quit
    with open("ip.txt", "r")as f:
        IP = f.readlines()
        if IP == "":
            print("Not found any ip in ip.txt file.")
            print("Please, remove or add the ip to that empty ip.txt file.")
            quit()

    # Creating a multi process with thread module to run scans all in one time
    fullScan = threading.Thread(target=full_scan, args=(IP))
    initScan = threading.Thread(target=init_scan, args=(IP))

    fullScan.start()
    initScan.start()

    fullScan.join()
    initScan.join()

    # Got to the final stage
    if "finalScan.sh" in os.listdir():
        subprocess.run(["bash", "finalScan.sh"])

        #with open("ports.list", "r") as f:
            #ports = str(f.readlines())
            #convert_to_readable = " ".join(ports)
            #convert_to_readable = ",".join(ports)
            #subprocess.run(["nmap", "-p", convert_to_readable, IP])
            #subprocess.run(["nmap", "-sVC", "-T5", "-Pn", "-oN", "nmap/final_scan", IP])


# Check for ip.txt file and create one if does not exist.
elif "ip.txt" not in os.listdir():
    print("""
          Only enter the IP address, or domain anything else 
          will lead to error.""")
    
    IP = str(input("$IP: "))
    
    with open("ip.txt", "a") as f:
        f.write(IP)

    fullScan = threading.Thread(target=full_scan, args=(IP))
    initScan = threading.Thread(target=init_scan, args=(IP))

    fullScan.start()
    initScan.start()

    fullScan.join()
    initScan.join()



# ENDING PORT SCAN SECTION



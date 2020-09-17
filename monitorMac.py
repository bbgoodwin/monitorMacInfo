#!/usr/bin/env python
import os
import psutil
import platform
from datetime import datetime
import re
import sys
import subprocess
import speedtest

def main():
    getCpuUsage()
    getMemoryUsage()
    getNetworkSpeed()

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def getCpuUsage():
    print("="*40, "CPU Info", "="*40)
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")

def getMemoryUsage():
    print("="*40, "Memory Information", "="*40)
    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")
    print(f"Available: {get_size(svmem.available)}")
    print(f"Used: {get_size(svmem.used)}")
    print(f"Percentage: {svmem.percent}%")

def getNetworkSpeed():
    print("="*40, "Network Speed", "="*40)
    s = speedtest.Speedtest()
    print(str(round(s.download()/(10**6), 2)) + " Mbps")
    print(str(round(s.upload()/(10**6), 2)) + " Mbps")

if __name__ == "__main__":
   main()

#print(os.system("powermetrics --samplers smc |grep -i \"CPU die temperature\""))

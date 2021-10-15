"""
# File : a1.py
# Created : 15-10-2021 09:36
# Author : Snehal Shirsath
# Python Version : 3.9.7
# File Version : v1.0.0
# Description :
"""
import platform
import socket
import sys

from tabulate import tabulate

# definition to get the details
def machineinfo():
    # get machine details
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    os_name = platform.system()
    Path = sys.path

    table = [['system name', host_name], ['system IP', host_ip], ['operation system', os_name], ['current path', Path[0]]]
    print(tabulate(table))


if __name__ == "__main__":
    machineinfo()

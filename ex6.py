#!/usr/bin/env python

# Use Paramiko to retrieve the entire 'show version' output from pynet-rtr2.

from netmiko import ConnectHandler
import time
from getpass import getpass
import yaml
from pprint import pprint

def main():

  with open("../store/inventory/devices.yml") as f:
    devices = yaml.load(f)
  
  pprint(devices)
  
  for device in devices['devices']:
    a_device = {
      'ip': device['ip_addr'],
      'username': device['username'],
      'password': device['password'],
      'device_type': device['device_type'],
      'port': 22    
    }

    net_connect = ConnectHandler(**a_device)
    output = net_connect.send_command("show arp")
    print()
    print('#'*80)
    print("Device:{}".format(net_connect.ip))
    print()
    print(output)
    print('#'*80)
    print()

if __name__ == "__main__":
    main()
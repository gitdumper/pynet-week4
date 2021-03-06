#!/usr/bin/env python

# Use Paramiko to change the 'logging buffered <size>' configuration on pynet-rtr2. 
# This will require that you enter into configuration mode.

import paramiko
import time
from getpass import getpass
import yaml

def main():

  with open("../store/inventory/devices.yml") as f:
    devices = yaml.load(f)

  print(devices['devices'][1])

  remote_conn_pre = paramiko.SSHClient()
  #remote_conn_pre.load_system_host_keys()
  remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

  ip_addr = devices['devices'][1]['ip_addr']
  username = devices['devices'][1]['username']
  password = devices['devices'][1]['password']
  port = 22

  remote_conn_pre.connect(ip_addr, port=port, username=username, password=password,
                            look_for_keys=False, allow_agent=False)
  remote_conn = remote_conn_pre.invoke_shell()

  time.sleep(1)
  output = remote_conn.recv(5000)

  remote_conn.send("show run | i logging\n")
  time.sleep(2)
  output = remote_conn.recv(5000).decode('utf-8', 'ignore')
  print(output)

  remote_conn.send("conf t\n")
  time.sleep(1)
  output = remote_conn.recv(5000)

  remote_conn.send("logging buffered 20011\n")
  time.sleep(1)
  output = remote_conn.recv(5000)

  remote_conn.send("end\n")
  time.sleep(1)
  output = remote_conn.recv(5000)

  remote_conn.send("show run | i logging\n")
  time.sleep(2)
  output = remote_conn.recv(5000).decode('utf-8', 'ignore')
  print(output)

if __name__ == "__main__":
  main()

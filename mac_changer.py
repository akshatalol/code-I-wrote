#!usr/bin/env python3
import subprocess

interface = input("Enter the interface name you want to change the MAC address for:")
new_mac = input("Enter the new MAC address in this form: 00:aa:bb:cc:dd:ee where a,b,c,d,e are alphanumeric characters:")
print("Changing the MAC address of "+interface+" to "+new_mac)
subprocess.call(["ifconfig", interface, "down"]) #list method is inefficient, but helps sanitise user input to avoid code injections
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

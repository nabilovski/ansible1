from netmiko import ConnectHandler
import csv
import re
import sys
# router1={
#         "device_type" : "cisco_ios",
#         "ip" : "192.168.122.101",
#         "username" : "nabil",    
#         "password" : "cisco",
#         "secret" : "secret"    

# }
# net_connect=ConnectHandler(**router1)
# ouptput=net_connect.send_command("show ip int b")
# print(ouptput)


SW1={
        "device_type" : "cisco_ios",
        "ip" : "192.168.122.110",
        "username" : "nabil",    
        "password" : "cisco",
        "secret" : "secret"    

}

SW2={
        "device_type" : "cisco_ios",
        "ip" : "192.168.122.111",
        "username" : "nabil",    
        "password" : "cisco",
        "secret" : "secret"    

}

SWx=[SW1,SW2]

for device in SWx:
    print("***** This is SWITCH: "+ str(device["ip"]))
    net_connect=ConnectHandler(**device)

    for i in range(2,5):
        config_commands=["vlan "+str(i), "name VLAN_"+str(i),  "exit"]
        config=net_connect.send_config_set(config_commands)
        print(config) # to see what's being configured in real time
    ouptput=net_connect.send_command("show cdp neighbors")
    print(ouptput)



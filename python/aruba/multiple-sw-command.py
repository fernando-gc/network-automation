# SSH to Multiple Devices from devices file
from netmiko import ConnectHandler

#First create the device object using
with open('devices.txt') as routers:
 for IP in routers:
        CSR = {
            'device_type': 'hp_procurve',
            'ip': IP,
        }

        net_connect = ConnectHandler(**CSR)

        print ('Connecting to ' + IP)
        output = net_connect.send_command('show running-config')


        print(output)
        print('-'*65)

# Finally close the connection
net_connect.disconnect()
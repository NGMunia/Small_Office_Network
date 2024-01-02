from netmiko import ConnectHandler
from rich import print as rp
from Network.Devices import Routers, Switches, Firewalls
from itertools import chain
from csv import writer


rp('[cyan]----------Device Inventory----------[/cyan]')
filepath = input('Inventory filepath: ')
with open (f'{filepath}/Data.csv', 'w')as f:
    write_data = writer(f)
    write_data.writerow(['Hostname','IP address','Software Image','Version','Serial number'])
    for devices in chain(Routers.values(), Firewalls.values(), Switches.values()):
        c = ConnectHandler(**devices)
        c.enable()
        output = c.send_command('show version',use_textfsm=True)[0]

        hostname = output['hostname']
        ip_addr  = devices['ip']
        image    = output['software_image']
        version  = output['version']
        serial   = output['serial']

        write_data.writerow([hostname,ip_addr,image,version,serial])
        rp(f'Finished taking {hostname} Inventory')
        c.disconnect()




print('\n')
rp('[cyan]----------Getting Devices\' running configurations----------[/cyan]')
filepath = input('Input backup filepath: ')
for devices in chain(Routers.values(), Firewalls.values(), Switches.values()):
    c = ConnectHandler(**devices)
    c.enable()
    host = c.send_command('show version',use_textfsm=True)[0]['hostname']
    output = c.send_command('show run')
    with open (f'{filepath}/{host}','w') as f:
        f.write(output)
        c.disconnect()
    rp(f'The running-configuration of ',host,' has been successfully backed up!!')





print('\n')
for devices in chain(Routers.values(), Firewalls.values(),Switches.values()):
    c = ConnectHandler(**devices)
    c.enable()
    output = c.send_command('show version', use_textfsm=True)[0]
    rp(f'[cyan]---------------{output["hostname"]}---------------[/cyan]\n')
    for key, value in output.items():
        rp((f'{key:>15} : {value}'))
    print('\n')      
    
     
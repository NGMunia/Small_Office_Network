from fastapi import FastAPI
from pydantic import BaseModel
from netmiko import ConnectHandler
from rich import print as rp
from Network.Devices import Routers, Firewalls, Switches

app = FastAPI()

#Device health API for Routers
@app.get('/Get/Devices/Routers/{Device_ID}/Health')
def Routerhealth(Device_ID: str):
    device = Routers[Device_ID]
    conn = ConnectHandler(**device)
    conn.enable()
    command = conn.send_command('show version',use_textfsm=True)
    return command


#Firewall Stateful inspecton status:
@app.get('/Get/Devices/Firewalls/{Device_ID}/Status')
def firewallstatus(Device_ID: str):
    device = Firewalls[Device_ID]
    conn = ConnectHandler(**device)
    conn.enable()
    command = conn.send_command('show policy-map type inspect zone-pair',use_textfsm=True)
    return command.splitlines()


#Getting Switch VLANs:
@app.get('/Get/Devices/Switches/{Device_ID}/VLANs')
def switchvlans(Device_ID: str):
    device = Switches[Device_ID]
    conn = ConnectHandler(**device)
    conn.enable()
    command = conn.send_command('show vlan brief',use_textfsm=True)
    return command
from Login import username, password, secret


Firewalls ={
            'FW1': {
                      'device_type':'cisco_ios',
                      'username': username,
                      'secret': secret,
                      'password': password,
                      'ip':'10.1.255.2'
                    },
            'FW2': {
                      'device_type':'cisco_ios',
                      'username': username,
                      'secret': secret,
                      'password': password,
                      'ip':'10.1.255.3'
                    }         
           }
Routers =  {
            'R1-LAN':{
                      'device_type':'cisco_ios',
                      'username': username,
                      'secret': secret,
                      'password': password,
                      'ip':'192.168.101.1',
                    },
            'R1-VPN':{
                      'device_type':'cisco_ios',
                      'username': username,
                      'secret': secret,
                      'password': password,
                      'ip':'10.1.1.1'
                    },
            'R2-VPN':{
                      'device_type':'cisco_ios',
                      'username': username,
                      'secret': secret,
                      'password': password,
                      'ip':'10.1.1.2'
                    }      
            }
Switches=   {
        'LAN-SW':  {
                      'device_type':'cisco_ios',
                      'username': username,
                      'secret': secret,
                      'password': password,
                      'ip':'192.168.100.10'
                   },
        'ISP-SW':  {
                      'device_type':'cisco_ios',
                      'username': username,
                      'secret': secret,
                      'password': password,
                      'ip':'10.1.255.10'
                   }
            }

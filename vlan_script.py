from netmiko import ConnectHandler
import getpass

password = getpass.getpass('Please enter the password: ') # Reads the output from the user and save it as a string

switch_list = ['10.10.20.18', '10.10.20.19', '10.10.20.20']
device_inventroy = []
vlans = {
    '10': 'MGMT',
    '20': 'DATA',
    '30': 'active_directory',
    '31': 'web_servers',
    '32': 'admin',
    '33': 'network'
    }

for ip in switch_list:
    device = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": "cisco",
        "password": password,
        "secret": password # Enable password
    }
    device_inventroy.append(device)

for switch in device_inventroy:
    connection = ConnectHandler(**switch)
    output = connection.send_command('show vlan', use_textfsm=True)
    connection.enable() # Enable method
    connection.config_mode() # Global config mode
    
    current_vlans_dict = {}
    for vlan in output:
        current_vlans_dict[vlan['vlan_id']] = vlan['name']

    for k,v in vlans.items():
        if k in current_vlans_dict and v != current_vlans_dict[k]:
            commands = [f"vlan {k}", f"name {v}"]
            config_output = connection.send_config_set(commands)
            print(config_output)

    connection.disconnect()
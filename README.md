## Overview
This Python script uses the Netmiko library to configure VLANs on Cisco IOS switches. It retrieves the list of VLANs currently configured on each switch, and compares it to a dictionary of VLANs that should be present. If a VLAN has a wrong name, the script changes the name. 

- Dictionary contains VLAN ID and the correct Name.
- If a particular VLAN doesn't exist on a switch, the script doesn't create it.
- If a particular VLAN does exist on a switch but has a wrong name, the script changes the name to the correct one.
- The script should never delete or create new VLANs.

## Prerequisites
- To use this script, you need to have Python 3.x installed, as well as the Netmiko library.
- You also need to have access to the switches you want to configure, and have the necessary credentials to log in and make changes.

## Usage
Clone this repository and navigate to the directory in your terminal.
Modify the `switch_list` variable to contain the IP addresses of the switches you want to configure.
Modify the `vlans` dictionary to contain the VLANs you want to configure, and their corresponding names.
Run the script by typing python `vlan_script.py` in your terminal.
The script will connect to each switch in `switch_list`, retrieve the list of VLANs currently configured, and configure misconfigured VLAN namess based on the vlans dictionary.

## Output
The script will output messages indicating which switch it is connecting to, which VLANs are being configured, and when it is disconnecting from each switch.

## Note
This script is provided as an example only, and should be modified to suit your specific requirements. Use at your own risk.

For more info - https://www.packetswitch.co.uk/using-python-to-standardize/
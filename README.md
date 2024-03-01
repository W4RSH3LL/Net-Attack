# Net-Attack Scripts -- Python3 🐍

## Installation ✅:
- `git clone https://github.com/W4RSH3LL/Net-Attack.git`
- `cd Net-Attack`
## Usage:
### To scan the network use the command:
- `sudo python3 net_scan.py -t target_ip` <--The target ip can also be the entire network
- example: `sudo python3 net_scan.py -t 192.168.1.1/24`

### To start the arp_spoof attack, use the command:
- `sudo python3 arp_spoof.py -t target_ip -gw gateway_ip`
- example: `sudo python3 arp_spoof.py -t 192.168.1.12 -gw 192.168.1.1`
  

## Help 🆘:
use:
`python3 mac_changer.py -h` or `--help` for more info.

## Libraries used in this program 📚📗:!
- `subprocess`
- `optparse`
- `scapy`
- `colorama`


## Screenshots 📷:

*Command to change MAC:*
 
![Pasted image 20240301100929 1](https://github.com/W4RSH3LL/MAC_Changer/assets/129652925/cfd76f8e-6e74-4518-bace-9f19d309831b)

*Output:*
  
![Pasted image 20240301102959 1](https://github.com/W4RSH3LL/MAC_Changer/assets/129652925/d84d1ecd-cdfb-4abb-aece-ac30ad11c629)

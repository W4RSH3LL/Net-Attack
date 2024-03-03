# Net-Attack Scripts -- Python3 🐍
![Net-Attack](https://github.com/W4RSH3LL/Net-Attack/assets/129652925/04d6c736-c0b9-4c32-8a0d-62bac4c98e9a)

## Installation ✅:
- `git clone https://github.com/W4RSH3LL/Net-Attack.git`
- `cd Net-Attack`
## Usage:
### To scan the network use the command:
- `sudo python3 net_scan.py -t target_ip` <--The target ip can also be the entire network
- example: `sudo python3 net_scan.py -t 192.168.1.1/24`

### To start the ARP Spoof attack, use the command:
- `sudo python3 arp_spoof.py -t target_ip -gw gateway_ip`
- example: `sudo python3 arp_spoof.py -t 192.168.1.12 -gw 192.168.1.1`

### To start the Packet Sniffer:
By default the interface is eth0, you can change it inside of the script.
- `sudo python3 packet_sniffer.py`

## Help 🆘:
use:
`python3 net_scan.py -h` or `--help` for more info.
`python3 arp_spoof.py -h` or `--help` for more info.

## Libraries used in this program 📚📗:!
- `subprocess`
- `argparse`
- `scapy`
- `colorama`

## Screenshots 📷:
*net_scan.py:*

![Pasted image 20240301165708](https://github.com/W4RSH3LL/Net-Attack/assets/129652925/818c7cab-d0da-4a74-befb-fb1179019ee9)

*arp_spoof.py:*

![Pasted image 20240301165920](https://github.com/W4RSH3LL/Net-Attack/assets/129652925/b9164392-97c2-447c-92bc-adc7817b6436)
![Pasted image 20240301165933](https://github.com/W4RSH3LL/Net-Attack/assets/129652925/11df2242-561a-4050-835e-0c39ba328c04)

![Net-Attack2](https://github.com/W4RSH3LL/Net-Attack/assets/129652925/ce1fba8f-def7-4615-bc50-7332f72468b5)

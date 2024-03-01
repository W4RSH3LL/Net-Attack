#!/usr/bin/env python
import scapy.all as scapy
import argparse
from colorama import Fore

# Get arguments + options from the user
def get_args():
    parser = argparse.ArgumentParser() # Creating parser objects
    parser.add_argument("-t", "--target", dest="target", help="Target IP('s) to use for scan") # Adding IP Range options to the parser object
    options =  parser.parse_args() # Returning Options & Arguments

    # Verifying for user input
    if not options.target:
        # Handle error
        parser.error(Fore.RED + "[-] Please enter an IP range or single IP to scan, use -h for more info [-]")
    else:
        return options # Returning the options and arguments from the parser

# Creating and sending the ARP scan packet
def scan(ip):
    clients_list = [] # Creating a list to contain the clients IP's and MAC Addr
    arp_request = scapy.ARP(pdst=ip) # Defining the IP of are Packet
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # Defining the Ether of are Packet
    arp_request_broadcast = broadcast/arp_request # Combining the Ether and IP to craft our packet
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0] # Using the send and receive    
    
    #Iterating through the answered packets list
    for element in answered_list: 
        client_dict = {"ip":element[1].psrc , "mac":element[1].hwsrc} # Creating a dictionnary for the clients
        clients_list.append(client_dict) # Appending the dictionnary to the list
    return clients_list
    
# Priting out the results list
def print_result(results_list):
    print(Fore.CYAN + "\n----------------------------------------------")
    print(Fore.CYAN + "        IP\t\t     MAC Address\n----------------------------------------------")
    for client in results_list:
        print(Fore.LIGHTGREEN_EX + f'[+] {client["ip"]} \t {client["mac"]} [+]')

# Calling the main function
if __name__ == "__main__":
    options = get_args()

scan_result = scan(options.target)
print_result(scan_result)
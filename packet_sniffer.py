#!/usr/bin/env python3
import scapy.all as scapy
from scapy.layers import http
from colorama import Fore, Back, Style

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet) #Sniffing the packets with the sniff function (iface is the interface to sniff, store is to store the packets, prn is the call back function to process the packets)

# Function to load keywords from a file
def load_keywords(file_path):
    with open(file_path, 'r') as file:
        keywords = [line.strip() for line in file.readlines()]
    return keywords

def get_url(packet):
    return packet[http.HTTPRequest].Host.decode('utf-8', errors='ignore') + packet[http.HTTPRequest].Path.decode('utf-8', errors='ignore')

def get_info(packet):
    if packet.haslayer(scapy.Raw): # Checking if the packet has a raw layer
           load = packet[scapy.Raw].load.decode('utf-8', errors='ignore')  # Saving the inside the load var raw layer (.load is the raw data) (load is a subfield of the raw layer) + Decoding the load to string
           keywords = load_keywords("keywords_lists/keywords.txt") # Loading the keywords from a file
           for keyword in keywords: # Checking if the keyword is in the keywords list
               if keyword in load: # Checking if the keyword is in the load var raw layer
                   return load

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):  # Checking if the packet is a HTTP Request
        url = get_url(packet)  # Getting the URL
        
        print(Fore.YELLOW + f'HTTP URL: {url}')  # Printing the URL
        info = get_info(packet)  # Getting the info
        if info:  # Checking if the info is not empty
            print(Fore.LIGHTGREEN_EX + f'[+] Info found! {info}\n')  # Printing the keyword found

network_interface = input("Enter the interface to sniff: ") # Getting the interface to sniff
print(Fore.LIGHTMAGENTA_EX + f'[+] Sniffing on {network_interface}...\n')
sniff(network_interface) # Sniffing the packets with the sniff function

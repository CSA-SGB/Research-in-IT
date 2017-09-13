'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>
'''

'''
Samantha Bennefield
9/8/17
Mr. Davis
Port Scanner
'''
import socket

#socket.error is an exception raised for socket-related errors

host = "127.0.0.1"
host2 = "172.17.2.87"

#The socket
x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#The common ports
common_ports = [9675, 21, 22, 23, 25, 53, 80, 110, 143]

def option3(): #User enters IP
    print("Scanning common ports:")
    for port in common_ports:
        try:
            s = x.connect((host, port))
            if s == 0:
                print(str(port)+" open")#Prints successful connections
                x.close()
        except socket.error: 
            print(str(port)+" closed")
            pass

    print("Scan more?")
    get_min_port = input("Enter a minimum port: ")
    minPort = int(get_min_port)

    get_max_port = input("Enter a maximum port: ")
    maxPort = int(get_max_port)
    for port in range(minPort, maxPort):
        try:
            s = x.connect((host, port))
            if s == 0:
                print(str(port)+" open")#Prints successful connections
                x.close()
        except socket.error: 
            print(str(port)+" closed")
            pass


def option2(): #Scans 172.17.2.87
    print("Scanning common ports:")
    for port in common_ports:
        try:
            s = x.connect((host2, port))
            if s == 0:
                print(str(port)+" open")#Prints successful connections
                x.close()
        except socket.error: 
            print(str(port)+" closed")
            pass

    print("Scan more?")
    get_min_port = input("Enter a minimum port: ")
    minPort = int(get_min_port)

    get_max_port = input("Enter a maximum port: ")
    maxPort = int(get_max_port)
    for port in range(minPort, maxPort):
        try:
            s = x.connect((host2, port))
            if s == 0:
                print(str(port)+" open")#Prints successful connections
                x.close()
        except socket.error: 
            print(str(port)+" closed")
            pass

def option1(): #Scans 127.0.0.1
    print("Scanning common ports:")
    for port in common_ports:
        try:
            s = x.connect((host, port))
            if s == 0:
                print(str(port)+" open")#Prints successful connections
                x.close()
        except socket.error: 
            print(str(port)+" closed")
            pass

    print("Scan more?")
    get_min_port = input("Enter a minimum port: ")
    minPort = int(get_min_port)

    get_max_port = input("Enter a maximum port: ")
    maxPort = int(get_max_port)
    for port in range(minPort, maxPort):
        try:
            s = x.connect((host, port))
            if s == 0:
                print(str(port)+" open")#Prints successful connections
                x.close()
        except socket.error: 
            print(str(port)+" closed")
            pass

def menu():
    IP = input("[1] Scan 127.0.0.1 \n[2] Scan 172.17.2.87 \n[3] Enter an IP \n")
    IP = int(IP)
    if IP == 1:
        option1()
    elif IP == 2:
        option2()
    elif IP == 3:
        option3()
    else:
        print("Invalid input. Try again.")
        menu()
        
        
menu()

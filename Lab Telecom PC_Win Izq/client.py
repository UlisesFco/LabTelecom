#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Carlos Mex Perera
"""

import socket
import json


HOST, PORT = "localhost", 6000
wsnQuery ='{"id": "neighbours", "mac": "0008"}'
# Queries
# {"id": "neighbours", "mac": "XXXX"}
# {"id": "all_neighbours", "mac": "XXXX"}
# {"id": "attached_devices", "mac": "XXXX"}
# {"id": "end_devices", "mac": "XXXX"}
# {"id": "routes", "mac": "XXXX"}

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(wsnQuery.encode())
    # Receive data from the server and shut down
    received = sock.recv(1024)
finally:
    sock.close()

jrec = json.loads(received) 
print (jrec)

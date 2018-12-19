#!/usr/bin/env python
import socket

print("[+] Waiting for incoming connection established")
# Creating socket listener
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Enable option if connection lost or drop the socket can be reuse
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("10.0.2.15", 4444))
listener.listen(0)

listener.accept()
print("[+] Connection established")
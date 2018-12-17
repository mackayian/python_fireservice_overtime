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
NOLONGER_NEEDED = "no longer needed"

# Search strings
# STRSTART = 'http://track=2Ebrandwee=\r\nrrooster=2Enl/track/click/30374404/www=2Efireservicerota='
STREND = '>Accept</a>'
STRENDNEW = "answer=accept"
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
f12.close()

intEmailCount = 0

print("This script is turned: " + strSwitch)

# whilst turned ON
while(strSwitch =="ON"):
	
	# Sleep for half second and re-read control file whilst in loop
	time.sleep(0.1)
	fControl = open(CONTROL_FILE_LOCATION)
	strSwitch = fControl.read()
	fControl.close()

	# log
	ts = time.time()
	strTime = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	strLog = strTime + " --> Refreshing emails..." + " \n"
	#f1 = open(LOG_FILE_LOCATION, "a+")
	#f1.write(strLog)
	#f1.close()
	
	print(strLog)
	
	# open emails
	M = imaplib.IMAP4_SSL(SMTP_SERVER)
	M.login(FROM_EMAIL, FROM_PWD)
	M.select('inbox')
	typ, data = M.search(None, 'UNSEEN')
	
	# loop through UNSEEN emails
	for num in data[0].split():
		typ, data = M.fetch(num, '(RFC822)' )

		for response_part in data:
			if isinstance(response_part, tuple):
				# search email msg
				strEmail = response_part[1].decode()
				strMsg = email.message_from_string(strEmail)
				print(strMsg['from'])
				
				# log
				ts = time.time()
				strTime = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
				strLog = strTime + " --> Unseen email from: " + strMsg['from'] + " \n"
				f1 = open(LOG_FILE_LOCATION, "a+")
				f1.write(strLog)
				#f1.write(strEmail)
				f1.close()
				
				#intEnd = strEmail.find(STREND) - 1
				intEnd = strEmail.find(STRENDNEW) + 13
				intEmailCount = intEmailCount + 1
				
				# New method for scanning for URL
				intH = 0
				intT1 = 0
				intT2 = 0
				intP = 0
				strH = "x"
				strT1 = "x"
				strT2 = "x"
				strP = "x"
				blnFoundHttp = 0
				intCount = intEnd
				intLastSMark = 0
				
				intNoLongerNeeded = strEmail.find(NOLONGER_NEEDED)
				
				# still needed?
				if intNoLongerNeeded == -1:
					# if ACCEPT link found
					if intEnd > 0:
						while(blnFoundHttp == 0):
							strP = strEmail[intCount]
							strT2 = strEmail[intCount - 1]
							strT1 = strEmail[intCount - 2]
							strH = strEmail[intCount - 3]	
							if strH =="h" and strT1 == "t" and strT2 == "t" and strP == "p":
								print("Found http - can extract link!")
								blnFoundHttp = 1
								intStart = intCount - 3
							else:	
								intCount = intCount - 1
							
							if intCount < 1:
								print("Didn't find http - can't extract link")
								blnFoundHttp = 1
								intEnd = 0
								
						if intEnd > 0:
							strURL = strEmail[intStart:intEnd]
							
							# Check if any special encoding needs sorting out
							if intStart > 0 and strURL.find("=2E") > 0:
								strURL = strURL.replace("=2E", ".")
								strURL = strURL.replace("=\r\n", "")
								strURL = strURL.replace("=3D", "=")
							
							print("The URL: \n" + strURL + "\n")
								
							# send web request
							req = urllib.request.Request(strURL, headers={'User-Agent' : "Magic Browser"}) 
							con = urllib.request.urlopen( req )
							resp = con.read()
							str1 = str(resp,'utf-8')
							print("\nResponse from server: \n\n" + str1 + "\n")
							if str1.find("already") == -1:
								strOutcome = "Response already recieved!"
							else:
								strOutcome = "Thanks for responding - check if you got the shift!"
							
							# log details
							print(strOutcome)
							ts = time.time()
							strTime = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
							strLog = strTime + "  --> " + "Response from server: " + "\n" + strOutcome + "\n"
							f1 = open(LOG_FILE_LOCATION, "a+")
							f1.write(strLog)
							f1.close()
						else:
							strNoGood = "Didn't extract URL - something went wrong"
							print(strNoGood)
							ts = time.time()
							strTime = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
							strLog = strTime + "  --> " + strNoGood + "\n"
							f1 = open(LOG_FILE_LOCATION, "a+")
							f1.write(strLog)
							#f1.write(strEmail)
							f1.write("\n")
							f1.close()
				else:
					strNoGood = "No longer needed for the shift"
					print(strNoGood)
					ts = time.time()
					strTime = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
					strLog = strTime + "  --> " + strNoGood + "\n"
					f1 = open(LOG_FILE_LOCATION, "a+")
					f1.write(strLog)
					f1.close()
	M.close()
	M.logout()
		
# log
ts = time.time()
strTime = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
strLog = strTime + " --> Emails found from target sender = " + str(intEmailCount)
f1 = open(LOG_FILE_LOCATION, "a+")
f1.write(strLog + " \n")
f1.close()

print("End of script.  Emails found = " + str(intEmailCount))
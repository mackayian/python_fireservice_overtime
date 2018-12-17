#####################################
## Instructions for Acceptlinkv5.py #
#####################################
----------
To prepare:
----------
Store the following 3 files:
AcceptLinkv5.py
log.txt
Control.txt

In your Python36-32 location:
e.g. C:\Users\<name here>\AppData\Local\Programs\Python\Python36-32

-----------
Description/guidlines:
-----------
The AcceptLinkv5 script comes with the following enhanced features:
1. It will continually loop round and recheck unseen emails every 1-3 seconds (constrained by the server processing time)
2. It is controlled by the Control.txt file.  The script will continue to execute and refresh whilst the value in Control.txt = ON
3. The URL search mechanism is more robust, and has some resilience for encoded HTML characters
4. Log.txt will record all activity and results - this file should periodically be emptied, as it will build up over time if the script is continually run, and will consume hard disk space

-----------
To adjust the scripts:
-----------
Control.txt: ON or OFF value used to control script
AcceptLinkv5.py: The following values need amending prior to executing the script, so they match the target email account and correct Python location:

* FROM_EMAIL  = "bmorfillsfrs@gmail.com"
* FROM_PWD    = "Maciscool2017"
* LOG_FILE_LOCATION = "C:\\Users\\mackayi\\AppData\\Local\\Programs\\Python\\Python36-32\\log.txt"
* CONTROL_FILE_LOCATION = "C:\\Users\\mackayi\\AppData\\Local\\Programs\\Python\\Python36-32\\control.txt"

----------
To execute:
----------
Replace location below with local machine location of Python36-32:

C:\Users\mackayi\AppData\Local\Programs\Python\Python36-32\python.exe "C:\\Users\\mackayi\\AppData\\Local\\Programs\\Python\\Python36-32\\AcceptLinkv5.py"

Copy and run from an MSDOS CMD (Microsoft DOS Command Window)

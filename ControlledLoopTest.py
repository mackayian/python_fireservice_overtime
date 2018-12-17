import time
CONTROL_FILE_LOCATION = "C:\\Users\\mackayi\\AppData\\Local\\Programs\\Python\\Python36-32\\control.txt"
intCount = 0
f1 = open(CONTROL_FILE_LOCATION)
strSwitch = f1.read()
f1.close()

#while(strSwitch =="ON"):
while(intCount < 10):
	time.sleep(1)
	intCount = intCount + 1
	print(str(intCount))
	f1 = open(CONTROL_FILE_LOCATION)
	strSwitch = f1.read()

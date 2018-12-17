CONTROL_FILE_LOCATION = "C:\\Users\\mackayi\\AppData\\Local\\Programs\\Python\\Python36-32\\ShiftRequest_Example.txt"

fControl = open(CONTROL_FILE_LOCATION)
strEmail = fControl.read()
fControl.close()

intEnd = strEmail.find("answer=accept") + 13
intEmailCount = 0 
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
intStart = 0

print(str(intEnd))
# if ACCEPT link found
if intEnd > 0:
	while(blnFoundHttp == 0):
		strP = strEmail[intCount]
		strT2 = strEmail[intCount - 1]
		strT1 = strEmail[intCount - 2]
		strH = strEmail[intCount - 3]
		if strH =="h" and strT1 == "t" and strT2 == "t" and strP == "p":
			print("Found html")
			blnFoundHttp = 1
			intStart = intCount - 3
		else:	
			intCount = intCount - 1
		if intCount < 1:
			print("Didn't find http")
			blnFoundHttp = 1
			intEnd = 0
	
	if intEnd > 0:
		print(str(intStart))
		print(str(intEnd))
		strURL = strEmail[intStart:intEnd]
		print(strURL)
	

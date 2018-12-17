intCount = 0
intStart = 0
intEnd = 0
intH = 0
intT1 = 0
intT2 = 0
intP = 0
strH = "x"
strT1 = "x"
strT2 = "x"
strP = "x"
blnFoundHttp = 0

strHTML = '<top><a style=3D"display:=\r\n inline-block; text-align: center; vertical-align: middle; -webkit-user-sel=\r\nect: none; -moz-user-select: none; -ms-user-select: none; user-select: none=\r\n; border-radius: 4px; background-color: green; color: white; text-decoratio=\r\nn: none; font-family: arial; font-weight: bold; margin: 0 40px 0 0; padding=\r\n: 6px 12px; border: 1px solid transparent;" href=3D"http://track=2Ebrandwee=\r\nrrooster=2Enl/track/click/30374404/www=2Efireservicerota=2Eco=2Euk?p=3DeyJz=\r\nIjoidmR2TjdzREl2YWlqOXZNbm1MVkJhRmt4ZDFvIiwidiI6MSwicCI6IntcInVcIjozMDM3NDQ=\r\nwNCxcInZcIjoxLFwidXJsXCI6XCJodHRwOlxcXC9cXFwvd3d3LmZpcmVzZXJ2aWNlcm90YS5jby=\r\n51a1xcXC9jb21tdW5pY2F0aW9uXFxcL21lc3NhZ2VfcmVjaXBpZW50c1xcXC9iN2Y3MTIwNmM4Y=\r\n2JlMDcwMWQ2OThkMzgwZWZiYTFjZWEwNDUyNTg1Mjk2N2EwNWU5YjIxZTkyNTQ2MDNhYWVmMzBi=\r\nZWIxYzBhZWRiOWZkOGVkNzAyOWNiNGFmM2M0ZTMzYTM4YTMwZjQ4Njc4YzBiZTkwZTE1ZDExOTJ=\r\nkZWRjOFxcXC9lbWJlZGRlZF9xdWVzdGlvbnNcXFwvMjkyNz9hbnN3ZXI9YWNjZXB0XCIsXCJpZF=\r\nwiOlwiY2QwZDViYWVjMzhmNDY0ZmEyN2ZiNDQ1NGExYjFhYmRcIixcInVybF9pZHNcIjpbXCJhY=\r\nTk2MDMzM2QzZGE1NDY4MDQwOTQxYmZiYmU4ODY1YjI2ZWI5NmM2XCJdfSJ9">Accept</a><a href="http://test.com">Reject</a></top>'

http://track.brandweerrooster.nl/track/click/30374404/www.fireservicerota.co.uk?p=eyJzIjoibkYwYUR4Z3NtUDl4bFg2TGcyeDdqSHpIVklvIiwidiI6MSwicCI6IntcInVcIjozMDM3NDQwNCxcInZcIjoxLFwidXJsXCI6XCJodHRwOlxcXC9cXFwvd3d3LmZpcmVzZXJ2aWNlcm90YS5jby51a1xcXC9jb21tdW5pY2F0aW9uXFxcL21lc3NhZ2VfcmVjaXBpZW50c1xcXC84NjM2ZmYxNzU0ZmUyMGVhNWY1OGNkNjUxNWY0MjQzNGE2NTcwNzVkZDIyYmI4ZWVmOGEzZDM5ODZjMmFkYjExZWExMmQxMGU3YTljMGM0MTI1MzM2ZTgyZmE5OGE0MDY5N2VlMjM3YzQ4MzlhYzVkYTBjNjljZWEyMGM5ODk1OVxcXC9lbWJlZGRlZF9xdWVzdGlvbnNcXFwvMzA3ND9hbnN3ZXI9YWNjZXB0XCIsXCJpZFwiOlwiMzFiNTA3ZDY5ZGM5NDI2ZjkyNjQ1ZDUwM2MxMTFjMTRcIixcInVybF9pZHNcIjpbXCJhYTk2MDMzM2QzZGE1NDY4MDQwOTQxYmZiYmU4ODY1YjI2ZWI5NmM2XCJdfSJ9
http://track=2Ebrandwee=\r\nrrooster=2Enl/track/click/30374404/www=2Efireservicerota=

intCount = strHTML.find('>Accept</a>')
intEnd = intCount - 1
print(str(intCount))
print(strHTML[1])
intCount = intCount - 1

while(blnFoundHttp == 0):
	strP = strHTML[intCount]
	strT2 = strHTML[intCount - 1]
	strT1 = strHTML[intCount - 2]
	strH = strHTML[intCount - 3]
	if strH =="h" and strT1 == "t" and strT2 == "t" and strP == "p":
		print("Found HTTP")
		blnFoundHttp = 1
		intStart = intCount - 3
	else:	
		intCount = intCount - 1

strURL = strHTML[intStart:intEnd]
print(strURL)
	

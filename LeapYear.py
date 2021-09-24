year = int(input("Enter a year: "))
a="Leap year"
b="Common year"
if year<1582:
    print("Not within the Gregorian calendar period")
    exit()
if year%4!=0:
    print(b)
elif year%100!=0:
    print(a)
elif year%400!=0:
    print(b)
else:
    print(a)

# leap year function

def isYearLeap(year):
    if ((year%400==0) or (year%100!=0) and (year%4==0)):
        return True
    else:
        return False
#
# put your code here
#

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")

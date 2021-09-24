# program to return day of the year by providing year, month and a day of month
def isYearLeap(year): # leap year function
    if ((year%400==0) or (year%100!=0) and (year%4==0)):
        return True
    else:
        return False
    
# function to return no. of days in a month for any pair of (yearç month).  
def daysInMonth(year, month):
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month in (4,6,9,11):
        return 30
    elif month==2:
        leap=isYearLeap(year) # calling one function fromm another
        if leap:  # if leap==True
            return 29
        else:
            return 28
# function to return the day of year, taking month of any year and any day of that month.
def dayOfYear(year, month, day):
    for i in range(1,month):
        d=daysInMonth(year, i)
        day+=d
    return day
# put your new code here
#

print(dayOfYear(2000, 12, 31))
# return the day of year for 26th december, 2000.
print(dayOfYear(2000, 12, 26)) 

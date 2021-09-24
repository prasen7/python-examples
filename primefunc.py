def isPrime(num):
    c=num//2
    if num<=1:
        return False
    if num in (2,3):
        return True
    if num>3:            
        for i in range(2,c+1):
            if num%i==0:
                return False
    return True
#
# put your code here
#

for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()
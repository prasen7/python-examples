# Capitalize
name=['martin','ranatunga']
for i in name:
    print(i.upper(), end=" ")

# Q. How many stars will be printed by below code?
i= 10
while i>0:
    i-=2
    print("*")
    if(i<=3):
        break
else:
    print("*") 

# Q. what will be the output? 
i=2
while True:
    if i%3 == 0:
        break
    print(i)
    i+=2

# program to take input from user and return odd/even
a=int(input("\nEnter a no: "))
print(["even","odd"][a%2])

# what should be the length of the list
b=[1,2,3,(),[],None]
print("lenghth of list b=[1,2,3,(),[],None]=",len(b))

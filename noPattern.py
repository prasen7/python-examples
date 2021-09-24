# RUN THE PROGRAM TO SEE THE PATTERN OF NUMBERS
a=int(input("enter: "))
d=a
rows=7
k=0
l=1
print(a)
for i in range(rows-1):
    if (i%2!=0):
        a=a*3
        k+=3
        for j in range(k):
            print(a+(2*j), end=" ")
        print()
    else:
        d*=2
        l*=2
        for j in range(l):
            print(d+j, end=" ")
        print()

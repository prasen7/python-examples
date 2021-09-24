x=int(input("enter 1st no: "))
y=int(input("ënter 2nd no: "))
z=x
x=y
y=z
print("swapped numbers-", x,y)
# print first 16 powers of 2
# demostrate for loop
pow = 1
for exp in range(16):
    print("2 to the power of", exp, "is", pow)
    pow *= 2

for i in range(5,-1,-1):
    print("The value of i is currently", i)

print(reversed(range(10)))
print(list(reversed(range(10))))



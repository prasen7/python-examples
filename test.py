#test for '=' vs 'is'
# test for end and sep parameters in print statement 
num1=17
num2=19
print(num1,num2, sep=", ")
print(num2-2 is num1, end=" ")
print(num2-2==num1)

# test for zip function
names=["alice", "bob", "charlie"]
ages=[25,31,23]
for name, age in zip(names, ages):
    print(f"Name:{name} Age:{age}")

x=[1,2,3]
y=[4,5,6]
for i, j in zip(range(len(x)), range(len(y))):
    print(str(i)+"/"+str(j))

# test for f-strings
# f-strings are evaluated at runtime 
for i, j in zip(names, ages):
    print(F"Hello, {i}. You are {j}") # works with 'F' and 'f' both

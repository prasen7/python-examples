# factorial program
def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

for n in range(1, 6):# testing
    print(n,"-->", factorialFun(n))

# factorial using recursion
# recursion- a technique where the function invokes itself.

def fact(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n*fact(n-1)

print(fact(5))
    

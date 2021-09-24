def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum
print("fibonacci series, first 9 terms :")
for n in range(1, 10): # testing
    print(n, "->", fib(n))

# using recursion, find nth term of fibonacci sequence

def fib1(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)
print(fib(9))

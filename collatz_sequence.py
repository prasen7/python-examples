# collatz hypothesis - In 1937, a German mathematician named Lothar Collatz
# formulated an intriguing hypothesis (it still remains unproven)
# which can be described in the following way:
# 1.starting with any positive, non-zero integer n
# 2. if n is even, then n=n/2
# 3. if n is odd, then n=3*n+1
# 4. repeat the step 2 and 3 untill n=1
# The sequence made in this way using any +ve, non-zero integer will always end in 1.
# collatz sequence using while loop
c0=int(input("enter a non-negative and non-zero integer: "))
counter=0
while c0 != 1:
    if c0%2==0:
        c0=c0//2
    elif c0&1:
        c0=3*c0+1
    print(c0, end=" ")
    counter+=1
print("\nSteps:",counter)

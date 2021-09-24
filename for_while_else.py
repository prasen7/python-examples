# The loop's else branch is always executed once
# regardless of whether the loop has entered its body or not.

i = 5
while i < 5: # while loop wont be executed
    print(i)
    i += 1
else:
    print("else:", i)
    # last value of i = 5

# 

i = 111
for i in range(5):
    print(i)
else:
    print("else:", i)
    # last value of i =  4

# Note: if the control variable doesn't exist before the loop starts,
# it won't exist when the execution reaches the else branch.


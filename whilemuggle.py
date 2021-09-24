secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
n=0
a=int(input("guess the secret number: "))
if a==777:
    print("Well done, muggle! You are free now.")
while a!=777:
    print("Ha ha! You're stuck in my loop!")
    n+=1
    if n<4:
        a=int(input("try to guess again: "))
    else:
        a=int(input("Keep trying: "))
    if a==777:
        print("Well done, muggle! You are free now.")
        break
    
    
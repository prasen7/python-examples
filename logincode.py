print("""....""")
id1="prasen7"
passw="TestYourLuck"
try_count=3
while True:
    if try_count==0:
        print("continuous 3 wrong entries.\nPlease try again later.")
        break
    if try_count<3:
        print("Please try again.")
    x=input("Username : ")
    y=input("password : ")

    if ((id1 != x and passw != y) or (id1 != x and passw == y)):
        print("No account found.")
        try_count-=1
    elif id1 == x and passw != y:
        print("Password is incorrect.")
        try_count-=1
    else:
        print("login successful")
        break

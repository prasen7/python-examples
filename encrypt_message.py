# Python code to encrypt the entered message
from string import ascii_lowercase
msg= input("Enter the message to encrypt :")
msg= msg.lower()
msg2= ""

for i in msg:
    if i in ascii_lowercase:
        i2=122-ord(i)
        msg2+=chr(i2+97)
    else:
        msg2+=i
print(msg2)
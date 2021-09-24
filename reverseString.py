def reverse(s):
    str1= ""
    for i in s:
        str1= i + str1
    return str1

def rev(s):
    return s[::-1]

s= input()
out=reverse(s)
print(out)
print(rev(s))
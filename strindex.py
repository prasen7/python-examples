# program to generate index of string
s= input('enter string: ')
l=len(s)
print(*s, sep="|")
print('='*(l*2-1))
print(*range(l))

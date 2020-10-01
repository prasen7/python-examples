def outer():
    i=5
    while True:
        yield lambda x,y=i:lambda b,a=y:a*b+i
        i+=1
it=iter(outer())
for i in range(3):
    print(next(it)(3)(2))

def myfun(word, flag):
    """ provide a string and a flag as inputs. If the flag is 0, then even
    characters are printed. If flag is 1, then odd characters are printed."""
    
    if flag==0:
        print(word[1::2])
    elif flag==1:
        print(word[::2])
    else:
        print("enter a string as word and 0 or 1 as flag value")
        print(list(sen.split()))

sen="i am prasen"  
while True:
    word=str(input("enter a word(to exit just press enter): "))
    if word=="":
        print("code execution stopped by user")
        break
    flag=int(input("enter flag value: "))
    myfun(word, flag)
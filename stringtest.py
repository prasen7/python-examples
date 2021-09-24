# program to test the no of even and odd indexed letters in the string entered by the user
test_cases=int(input())  # how many times to run the program
for num in range(test_cases):    # loop to run the program 'test_cases' no of times
    word=input()  
    even=''  # to store even indexed letters in the string entered by the user
    odd=''   # to store odd indexed letters in the string entered by the user
    for index in range(len(word)):
        if index%2==0:
            even+=word[index]
        else:
            odd+=word[index]

    print('Odd index letters: {}, Even indexed letters: {}'.format(even, odd))

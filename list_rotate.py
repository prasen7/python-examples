# Provided with an integer array A of size N and an integer K
# print the array rotated in the right direction by K steps and then print the resultant array.
# First integer t denotes the no of test cases to run (entered by user)
# take the input of arrays in a single line using map function

print("list right rotation program: ")
# 1st approach
print("approach 1 : not altering the list but only printing elements in the req. order")
t = int(input("test cases: "))
while (t!=0):
    n,k=map(int, input("n and k: ").split())
    array=list(map(int, input("array: ").strip().split()))[:n]
    index = n - (k%n)
    for i in range(index, n):
        print (array[i], end=" ")
    for i in range(index):
        print (array[i], end=" ")
    print ("")

    t-=1
# 2nd aproach
print ("\napproach 2 to right rotate the list by 2 positions : list1=(list1[n-2:n]+list1[0:n-2]) \n also can be done with: list1 = (list1[-2:] + list1[:-2])")
list1=[1,2,3,4,5]
print ("list before rotation: {}".format(list1))
n = len(list1)
list1=(list1[n-2:n]+list1[0:n-2])
print ("list after right rotation by 2: {}".format(list1))


#3rd approach
print ("\napproach 3 to right rotate the list by 2 positions : functional  ")
def rotateright(lists, num):
    o=[]
    for item in range(len(lists) - num, len(lists)):
        o.append(lists[item])
    for item in range(0, len(lists) - num): 
        o.append(lists[item])
    return o

list2 = [2,3,4,5,6]
print("\nlist: {}".format(list2))
num = int(input("Enter num to right rotate the list: "))
print(rotateright(list2,num ))




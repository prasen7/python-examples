# removing duplicate from list  
# using collections.OrderedDict.fromkeys() 
from collections import OrderedDict 
  
# initializing list 
test_list = [1, 5, 3, 6, 3, 5, 6, 1] 
print ("The original list is : " +  str(test_list)) 
  
# using collections.OrderedDict.fromkeys() 
# to remove duplicated  
# from list  
res = list(OrderedDict.fromkeys(test_list)) 
  
# printing list after removal  
print ("The list after removing duplicates using OrderedDict : " + str(res)) 

#---------------------------------------------
myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

res=[]
for i in myList:
    if i not in res:
        res.append(i)
#
print("original list: ",myList)
print("The list with unique elements only with naive method: "+str(res))

#---------------------------------------------------------------
# another way to remove duplicate elements from the list
mylist = ["a", "c", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
# convert list to dictionary keys, as dictionary only has unique keys
# and then convert it back to list
print("unique list using dict:", mylist)
#--------------------------------------------------------------------
# using list comprehension 
# to remove duplicated  
# from list  
res = []
[res.append(x) for x in test_list if x not in res] 
# printing list after removal  
print ("The list after removing duplicates using list comprehension : " + str(res))
#---------------------------------------------------------------

# using set() 
  
# initializing list 
test_list = [1, 5, 3, 6, 3, 5, 6, 1] 
print ("The original list is : " +  str(test_list)) 
 
test_list = list(set(test_list)) 
  
# printing list after removal  
# DRAWBACK- distorted ordering as setS do not have order
print ("The list after removing duplicates with set: " + str(test_list))
# CAUTION- list order is lost.

#-----------------------------------------  
# using list comprehension + enumerate() 

test_list = [1, 5, 3, 6, 3, 5, 6, 1] 
print ("The original list is : " +  str(test_list)) 
  
# using list comprehension + enumerate() 
# to remove duplicated from list  

res = [i for n, i in enumerate(test_list) if i not in test_list[:n]] 
  
# printing list after removal
print("using list comprehension + enumerate()")
print ("The list after removing duplicates : " + str(res))

#---------------------------------------------------------


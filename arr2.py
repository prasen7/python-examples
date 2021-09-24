# Program to calculate buying and selling day for an item to achieve 
# maximum profit from a given array of prices of that item on different
# days.
 
def maxdiff(arr, arrsize):
    max1 = arr[1] - arr[0]
    a,b=0,0
    for i in range(0, arrsize):
        for j in range(0, arrsize):
            if (arr[j]-arr[i]>max1):
                max1=arr[j]- arr[i]
                a=i
                b=j
    print("buy day= {}, buying price={}, sell day={}, selling price={}, maximum profit={}".format(a+1,arr[a],b+1,arr[b],max1))
    
arr= [62, 67, 78, 98, 89, 34]
size= len(arr)
maxdiff(arr, size)        

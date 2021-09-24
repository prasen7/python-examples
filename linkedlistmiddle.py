# Singly linked list program (only one link between any two data elements)
# insert element in between two data nodes
# Create a node objet 
class Node:
    def __init__(self, dataval=None):
        self.dataval=dataval
        self.nextval=None
# create a class to use node object        
class SlinkedList:
    def __init__(self):
        self.headval=None 

# function to add new node in between
    def Inbetween(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent.")
            return
        NewNode=Node(newdata)
        NewNode.nextval=middle_node.nextval
        middle_node.nextval=NewNode 
        
    def listprint(self):  #Method for Traversing a linked list
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval

       
            
list1=SlinkedList()
list1.headval=Node("Mon")
e2=Node("Tue")
e3=Node("Wed")

list1.headval.nextval=e2  # link first node to second node
e2.nextval=e3  # link second node to third node

list1.Inbetween(list1.headval.nextval, "Fri")

list1.listprint()
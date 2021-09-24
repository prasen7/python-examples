# Singly linked list program (only one link between any two data elements)
# Singly linked list can only be traversed in forward direction starting from 1st data element
# Create a node objet 
class Node:
    def __init__(self, dataval=None):
        self.dataval=dataval
        self.nextval=None
# create a class to use node object        
class SlinkedList:
    def __init__(self):
        self.headval=None  
        
    def listprint(self):  #Method for Traversing a linked list
        printval=self.headval
        while printval is not None:
            print(printval.dataval, end=" ")
            printval=printval.nextval
        print("\n")
    def AtBegining(self, newdata): # method to insert element at the begining of the linked list
        NewNode=Node(newdata)
        # update the new node next val to existing node
        NewNode.nextval=self.headval
        self.headval=NewNode
    def AtEnd(self, newdata):  # method to insert element at end of the linked list
        NewNode= Node(newdata)
        if self.headval is None:
            self.headval=NewNode
            return
        laste=self.headval
        while(laste.nextval):
            laste=laste.nextval
        laste.nextval=NewNode
    def RemoveNode(self, removekey):  # function to remove node
        head= self.headval
        if (head is not None) and (head.dataval==removekey):
                self.headval=head.nextval
                head=None
                return
        while (head is not None):
            if head.dataval==removekey:
                break
            prev=head
            head=head.nextval
        if (head==None):
            return
        prev.nextval=head.nextval
        head=None
                    
            
list1=SlinkedList()
list1.headval=Node("Mon")
e2=Node("Tue")
e3=Node("Wed")

list1.headval.nextval=e2  # link first node to second node
e2.nextval=e3  # link second node to third node
list1.listprint()

list1.AtBegining("Sun") # insert element at the begining of the linked list
list1.AtEnd("Thu")  # insert element at the end of the linked list
list1.listprint()

list1.RemoveNode("Tue") # Remove node with key = Tue
list1.listprint()

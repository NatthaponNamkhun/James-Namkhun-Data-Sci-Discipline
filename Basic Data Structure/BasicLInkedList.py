class Node:
    def _init_(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        
class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

list = SLinkedList()
list.headval = Node("January")
n2 = Node("February")
n3 = Node("March")
n4 = Node("April")

# Linked a first Node to second Node
list.headval.nextval = n2

# Linked to other Node
n2.nextval = n3
n3.nextval = n4

list.listprint()
class node :
    def __init__(self,dataVal=None) :
        self.dataval=dataVal 
        self.nextval=None

class sLinkedlist :
    def __init__(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while(printval is not None):
            print(printval.dataval)
            printval=printval.nextval

list1=sLinkedlist()
list1.headval=node('mon')
e2=node('tue')
e3=node('wed')
list1.headval.nextval=e2
e2.nextval=e3
list1.listprint()
from ast import Break


class node :
    def __init__(self,data=None):
        self.data=data
        self.next=None
class slinkedlist :
    def __init__(self) :
        self.head=None
    def Atbeginig(self,data_in):
        Newnode=node(data_in)
        Newnode.next=self.head
        self.head=Newnode
    def RemoveNode (self,Removekey) :
        headval=self.head
        if(headval is not None):
            if(headval.data==Removekey):
                self.head=headval.next
                headval=None
                return
        while(headval is not None):
            if(headval.data==Removekey):
                Break
            prev=headval
            headval=headval.next
        if(headval==None):
            return
        prev.next=headval.next
        headval=None
    def listprint(self):
        printval=self.head
        while(printval):
            printval=self.head
            while(printval):
                print(printval.data)
                printval=printval.next
list1=slinkedlist()
dec=list1.Atbeginig('dec')
nov=list1.Atbeginig('nov')
oct=list1.Atbeginig('oct')
sep=list1.Atbeginig('sep')
list1.RemoveNode('dec')
list1.listprint()
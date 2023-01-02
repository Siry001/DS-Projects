


class stack :

    def __init__(self,limit=10) -> None:
        self.stk=[]
        self.limit=limit

    def push(self,item):
        if len (self.stk)>=self.limit:
            print('stck over flow')
        else:
            self.stk.append(item)
        print('stack after push',self.stk)

    def pop(self):
            if len(self.stk)<=0:
                print('stack under flow')
            else:
                    return self.stk.pop()

def pal(y,leghnth):
        p=False
        s=stack( leghnth)
        for c in y :
            s.push(c)
        for c in y:
            if c==s.pop():
                p=True
            else:
                p=False
                break
        return p
    
x=input('enter your string for a palidrome')
if pal(x,len(x)):
    print('string is palindrome')
else:
    print('string is not palindrome')
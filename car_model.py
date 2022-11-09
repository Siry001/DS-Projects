class car:
    def __init__(self,name,tires,widith,height,status):
                self.name=name
                self.tires=tires
                self.widith=widith
                self.height=height
                self.status=status
    def modeling(status):
        print('the model name is : ',ob1.name)
        print('the tiers type is : ',ob1.tires)
        print('the car widith is : ',ob1.widith)
        print('the car height is : ',ob1.height)
        print('the car is : ',ob1.status )

x=str(input('enter the model name : '))
y=str (input('enter the tires type : '))
z=str(input('enter the widith of car : '))
e=str(input('enter the height : '))
h= str(input('enter the car state : '))

ob1=car(x,y,z,e,h)
car.modeling(status=ob1.status)
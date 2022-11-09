def fact (x):
    y=1
    for i in range(1,x+1):
        y=y*i
    print('the factorial number is :',y)
number=int(input('enter the number'))
fact(number)
#local variables
def display():
    a=10
    print("inside values is:",a)
display()


#global variables
x=10
def display():
    print("inside fun:",x)
display()
print("outside fun:",x)

#local vs global
x=100
def display():
    x=10
    print("the value for inside:",x)
display()
print("the value for outside:",x)

# change global variable values
y=20
def change():
    y=40
    print(y)
change()

#top-bottom
def add(a,b):
    return a+b
x=int(input("enter x value"))
y=int(input("enter y value"))
result=add(x,y)
print(result)

#recursion


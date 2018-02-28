from pythonds.basic.stack import Stack
import turtle
c=Stack()
def tostr(n,base):
    covertString="0123456789ABCDEF"
    while n>0:
        if n<base:
            c.push(covertString[n])
        else:
            c.push(covertString[n%base])
        n=n//base
    res=""
    while not c.isEmpty():
        res=res+str(c.pop())

    return res

print(tostr(234324,16))
print(30%2)
myTurtle=turtle.Turtle()
myWin=turtle.Screen()

def drawSpiral(myTurtle,lineLen):
    if lineLen>0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-2)

drawSpiral(myTurtle,200)
myWin.exitonclick()
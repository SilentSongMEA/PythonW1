import csv
import turtle

turtle.pencolor("white")
turtle.bgcolor("black")
def gotomap(a,b):
    turtle.penup()
    turtle.goto(a,b)
    turtle.pendown()
def colorb(c):
    turtle.fillcolor(c)
    turtle.begin_fill()
turtle.pensize(3)
turtle.ht()
turtle.speed("fast")
turtle.fillcolor("light blue")

def re(a):
    for i in range(4):
        turtle.forward(a)
        turtle.right(90)

gotomap(-170,-20)
f=open("C:\\Users\Abouzarrayaneh\\Videos\\pythonC6_140305012\\ex1.csv","r")
c=csv.reader(f)
listsum=[]
sum0=0

def g(a):
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(int(a))
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(int(a))
    turtle.left(90)
    turtle.forward(10)


turtle.begin_fill()
for i in c:
    for j in i[1:]:
        sum0+=int(j)
    listsum.append(sum0)
    g(sum0)
    print(i[0],"Hopop 6: ",sum0)
    sum0=0
turtle.end_fill()


gotomap(-250,-280)
colorb("green")
print("Max salary:",g(max(listsum)))
turtle.end_fill()

colorb("red")
print("Min salary:",g(min(listsum)))
turtle.end_fill()

colorb("green")
gotomap(10,-100)
re(70)
turtle.write(max(listsum),align='center',font=("tahoma",20))
turtle.end_fill()

colorb("red")
gotomap(10,-200)
re(70)
turtle.write(min(listsum),align='center',font=("tahoma",20))
turtle.end_fill()

turtle.done()





    



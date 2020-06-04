import turtle
import time
import random

delay = 0.1

#Score
score=0
high_score=0

#Set up the screen
wn=turtle.Screen()
wn.title("Snake game by Dipan Ghosh")
wn.bgcolor("black")
wn.setup(width=900,height=800)
wn.tracer(0)       #Turn off screen updates

#Snake Head
head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("grey")
head.penup()
head.goto(0,0)
head.direction="stop"

#Snake Food
food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(350,200)

segments=[]

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,360)
pen.write("SCORE: 0    HIGH SCORE: 0",align="center",font=("Courier",24,"bold"))


#Function
def go_up():
    if head.direction !="down":
        head.direction ="up"
    
def go_down():
    if head.direction !="up":
        head.direction ="down"
    
def go_left():
    if head.direction !="right":
        head.direction ="left"
    
def go_right():
    if head.direction !="left":
        head.direction ="right"
    

def move0():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)

def move1():
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
        
def move2():
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
        
def move3():
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
        
#Keyboard Bindings
wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")


#Main game loop
while True:

    wn.update()
    
    #Check for collision with the border
    if head.xcor()>430 or head.xcor()<-430 or head.ycor()>390 or head.ycor()<-390:
        time.sleep(1)
        head.goto(0,0)
        head.direction ="stop"
        
        
        #Hide segments
        for segment in segments:
            segment.clear()
            segment.ht()
            
        #Clear the segment list
        segments.clear()

        #Reset the score
        score=0

        #Reset the delay
        delay=0.1

        pen.clear()
        pen.write("SCORE: {}    HIGH SCORE: {}".format(score, high_score), align="center", font=("Courier", 24, "bold"))
    
    #Check for a collision with the food      
    if head.distance(food)<20:
        #Move the food to a random spot
        x=random.randint(-440,440)
        y=random.randint(-390,390)
        food.goto(x,y)
        ""
        #Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)
        
        #Shorten the delay
        delay-=0.01

        #Increase the score
        score+=10
        
        if score>high_score:
            high_score=score
        
        pen.clear()    
        pen.write("SCORE: {}    HIGH SCORE: {}".format(score,high_score),align="center",font=("Courier",24,"bold"))
        
        
    #Move the end segment first in the reverse order
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor
        y=segments[index-1].ycor
        segments[index].goto(x,y)
        
    #Move segment 0 to where the food is
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    
    move0()
    move1()
    move2()
    move3()
    
    
    time.sleep(delay)



wn.mainloop()
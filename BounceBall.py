import turtle
import random
import time

frame = turtle.Screen()
frame.title("Bounce Ball")
frame.bgcolor("black")
frame.setup(width=500,height=500)
frame.tracer(0)

paddle = turtle.Turtle()
paddle.speed(1)
paddle.shape('square')
paddle.color('white')
paddle.shapesize(stretch_wid=0.5,stretch_len=5)
paddle.penup()
paddle.goto(-200,-200)

ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')

ball.penup()
ball.goto(0,200)
ball.dx=2
ball.dy=-2


def moveRight():
    x=paddle.xcor()
    x+=10   
    paddle.setx(x)

def moveLeft():
    x=paddle.xcor()
    x-=10
    paddle.setx(x)


frame.listen()
frame.onkeypress(moveRight,'Right')
frame.onkeypress(moveLeft,'Left')

cor = random.randint(-280,280)
ball.setx(cor)
ball.sety(250)
score=0
while True:
    frame.update()
  
    ball.sety(ball.ycor()+ball.dy)
    ball.setx(ball.xcor()+ball.dx)
    time.sleep(0.005)
    
    if ball.xcor()>250:
        ball.dx *=-1
    
    if ball.xcor()<-250:
        print(ball.xcor())
        ball.dx*=-1
    
    if ball.ycor()<-250:
        ball.dy*=-1
        ball.sety(ball.ycor()+ball.dy)
    
    if ball.ycor()>250:
        ball.dy*=-1
        ball.sety(ball.ycor()+ball.dy)
    
       
        
        
    
    #print(paddle.ycor(),paddle.xcor())
    if (ball.dy<0 and ball.ycor()<=-185 and ball.ycor()>=-200) and(paddle.xcor()-10 <= ball.xcor() <= paddle.xcor()+10):
        ball.dy*=-1
        
        score =score+1
        print("score:",score)
    
       
   

       
        
    

        
    
    
    
    

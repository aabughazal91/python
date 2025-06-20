# simple ping pong game using the turtle module in Python.
import turtle
import time  

wind = turtle.Screen()  
wind.title("Ping Pong ") 
    
wind.bgcolor("grey") 

wind.setup(width=800, height=600) # Set the size of the window
wind.tracer(0) # Disable automatic screen updates for better performance

# racket 1
racket1 = turtle.Turtle()  
racket1.speed(0)  
racket1.shape("square")  
racket1.color("blue")  
racket1.shapesize(stretch_wid=5, stretch_len=1)  
racket1.penup()  
racket1.goto(-350, 0)  
    
# racket 2
racket2 = turtle.Turtle()  
racket2.speed(0)  
racket2.shape("square")  
racket2.color("red") 
racket2.shapesize(stretch_wid=5, stretch_len=1)  
racket2.penup()  
racket2.goto(350, 0)  
    
    # ball
ball = turtle.Turtle()  
ball.speed(0)  
ball.shape("circle")  
ball.color("red")  
ball.penup()  
ball.goto(0, 0)  
ball.dx = 2.5 
ball.dy = 2.5

#Score
score1 = 0
score2 = 0
score = turtle.Turtle()  
score.speed(0)  
score.color("black")  
score.penup()  
score.hideturtle()  
score.goto(0, 260)  
score.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))  


#function
def racket1_up():
    y = racket1.ycor()  # Get the current y-coordinate of the paddle
    if y < 250:  # Check if the paddle is not at the top edge
        y += 20  # Move the paddle up by 20 units
        racket1.sety(y)  # Update the paddle's position
        

def racket1_down():
    y = racket1.ycor()  
    y -= 20  
    racket1.sety(y)  
    
def racket2_up():
    y = racket2.ycor()  
    if y < 250:  
        y += 20  
        racket2.sety(y)  
        

def racket2_down():
    y = racket2.ycor()  
    if y > -250: 
        y -= 20  
    racket2.sety(y)  
        
# keyboard binding 
wind.listen()  # Listen for keyboard events
wind.onkeypress(racket1_up, "w")  # Bind the 'w' key to move madrab1 up
wind.onkeypress(racket1_down, "s")  # Bind the 'w' key to move madrab1 up
wind.onkeypress(racket2_up, "Up")  # Bind the 'w' key to move madrab1 up
wind.onkeypress(racket2_down, "Down")  # Bind the 'w' key to move madrab1 up

while True:
    wind.update()  # Update the screen continuously
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)  # Update the x-coordinate of the ball
    ball.sety(ball.ycor() + ball.dy) 
    time.sleep(0.01)# Update the y-coordinate of the ball  
    # Border checking
    if ball.ycor() > 290:  # Check if the ball is at the top edge
        ball.sety(290)  # Set the y-coordinate to the top edge
        ball.dy *= -1  # Reverse the y-axis speed of the ball

    if ball.ycor() <-290:  # Check if the ball is at the top edge
        ball.sety(-290)  # Set the y-coordinate to the top edge
        ball.dy *= -1  # Reverse the y-axis speed of the ball
        
    if ball.xcor() > 390:  # Check if the ball is at the right edge
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()# Increment the score for player 1
        score.write("Player 1: {}  Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))  # Write the initial score
    if ball.xcor() < -390:  # Check if the ball is at the left edge
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()# Increment the score for player 1
        score.write("Player 1: {}  Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
    # Paddle and ball collisions
    if (ball.xcor()> 340 and ball.xcor() < 350) and (ball.ycor() < racket2.ycor() + 50 and ball.ycor() > racket2.ycor() - 50):
        ball.setx(340)  # Set the x-coordinate to the right edge
        ball.dx *= -1  # Reverse the x-axis speed of the ball
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < racket1.ycor() + 50 and ball.ycor() > racket1.ycor() - 50):
        ball.setx(-340)  # Set the x-coordinate to the left edge
        ball.dx *= -1  # Reverse the x-axis speed of the ball
    
    
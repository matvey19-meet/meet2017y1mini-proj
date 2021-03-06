         #BUILDING SNAKE#
import turtle
import random#needed for later


turtle.bgcolor("black")

turtle.tracer(1,0) # This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X,SIZE_Y)  ##Turtle window size

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 8

#Initialize lists

pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.color("green")
snake.shape("square")



UP_EDGE =250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400


turtle.hideturtle()
#___________________________________________________________
Start_pos = snake.pos()

for i in range(START_LENGTH):

    x_pos = snake.pos()[0]
    y_pos = snake.pos()[1]
    x_pos+= SQUARE_SIZE

    my_pos=(x_pos,y_pos)
    snake.goto(x_pos,y_pos)

    #append the new position tuple to pos_list
    pos_list.append(my_pos)

    snake_stamp1 = snake.stamp()
    stamp_list.append(snake_stamp1)


#______#MOVE AROUND#______#

UP_ARROW = "Up"
LEFT_ARROW = "Left"   
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"

TIME_STEP = 100

SPACEBAR = "space"

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

direction = UP

def up():
    global direction
    direction=UP
    print("You pressed the up key")
    
def left():
    global direction
    direction=LEFT
    print("You pressed the left key")

def down():
    global direction
    direction=DOWN
    print("You pressed the down key")

def right():
    global direction
    direction=RIGHT
    print("You pressed the right key")


def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left")
    elif direction==UP:
        snake.goto(x_pos, SQUARE_SIZE + y_pos)
        print("You moved up")
    elif direction==DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)

    my_pos=snake.pos()
    pos_list.append(my_pos)

    snake_stamp2 = snake.stamp()
    stamp_list.append(snake_stamp2)

    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)

    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    #The 3 lines check if the snake is hitting the
    #right edge

    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        quit()
    if new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        quit()
    if new_y_pos >= UP_EDGE:
        print("You hit the up edge! Game over!")
        quit()
    if new_y_pos <= DOWN_EDGE:
        print("You hit the down edge! Game over!")
        quit()
    turtle.ontimer(move_snake,TIME_STEP)


move_snake()

turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)

turtle.listen()
































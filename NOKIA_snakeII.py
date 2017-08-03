         #BUILDING SNAKE#
import turtle
import random#needed for later


turtle.bgcolor("black")#BACKROUND COLOUR

turtle.tracer(1,0) # This helps the turtle move more smoothly

#Set up positions (x,y) of boxes that make up the snake
SIZE_X=1000
SIZE_Y=700
turtle.setup(SIZE_X,SIZE_Y)  ##Turtle window size

turtle.penup()

c = 0#SEE move.snake()


SQUARE_SIZE = 20
START_LENGTH = 1

#Initialize lists

pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#SNAKE SHAPE>>>
turtle.register_shape("green.gif")
snake = turtle.clone()
snake.shape("green.gif")
turtle.color("white")


#BORDER CONTROL><
UP_EDGE =250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

border = turtle.clone()
border.hideturtle()
border.goto(400, 250)
border.pendown()
border.goto(400,-250)
border.goto(-400,-250)
border.goto(-400, 250)
border.goto(400,250)
border.penup()

turtle.hideturtle()


turtle.penup()
#CONSRUCTS SNAKE_
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
    if direction !=DOWN:
        direction = UP
    print("You pressed the up key")
    
def left():
    global direction
    if direction != RIGHT:
        direction = LEFT
    print("You pressed the left key")

def down():
    global direction
    if direction!=UP:
        direction = DOWN
    print("You pressed the down key")

def right():
    global direction
    if direction!=LEFT:
        direction=RIGHT
    print("You pressed the right key")


#FOOD
turtle.register_shape("trash.gif")
food= turtle.clone()
food.shape("trash.gif")


turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)

turtle.listen()

def make_food():
    global food_stamps, food_pos
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/2.6/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2.6/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2.6/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2.6/SQUARE_SIZE)-1

    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

    food.goto(food_x, food_y)
    new_food_pos = (food_x, food_y)
    food_pos.append(new_food_pos)
    food_stamp_id = food.stamp()
    food_stamps.append(food_stamp_id)

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
    ###################################
    global food_stamps, food_pos

    if snake.pos() in food_pos:
        
        print(food_stamps)
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind]) #REMOVES EATEN FOOD STAMPS
        food_pos.pop(food_ind) #REMOVE ESTEN FOOD POSITION
        food_stamps.pop(food_ind)#REMOVE EATEN FOOD STAMP
        print("You have eaten the food!")
        make_food() 
        global c                #SCORE
        c = c+1                 #
        turtle.goto(-300, 200)
        turtle.clear()
        turtle.write(c)
    else:
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
    
    
    if pos_list[-1] in pos_list[0:-1]:
        print("You ate yourself!")
        quit()
    
    
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

    if pos_list[-1] in pos_list[0:-1]:
        print("You ate yourself!")
        quit()
            

make_food()
move_snake()

##food.hideturtle()
##
##
##
##
##
##
##
##turtle.mainloop()



























import turtle

#Named constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BULLSEYE_RADIUS = 25
RING1_RADIUS = 300
RING2_RADIUS = 200
RING3_RADIUS = 100
FORCE_FACTOR = 30
PROJECTILE_SPEED = 1
TARGET_LLEFT_X = 100
TARGET_LLEFT_Y = 250
TARGET_WIDTH = 25
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

#Set the graphics window size
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
turtle.speed(0)
turtle.hideturtle()

#Draw ring 1
turtle.penup()
turtle.goto(0, -RING1_RADIUS)
turtle.fillcolor('black')
turtle.pendown()
turtle.begin_fill()
turtle.circle(RING1_RADIUS)
turtle.end_fill()

#Draw ring 2
turtle.penup()
turtle.goto(0, -RING2_RADIUS)
turtle.fillcolor('white')
turtle.begin_fill()
turtle.circle(RING1_RADIUS)
turtle.end_fill()

#Draw ring 3
turtle.penup()
turtle.goto(0, -RING3_RADIUS)
turtle.fillcolor('black')
turtle.pendown()
turtle.begin_fill()
turtle.circle(RING3_RADIUS)
turtle.end_fill()

#Draw the bullseye
turtle.penup()
turtle.goto(0, -BULLSEYE_RADIUS)
turtle.fillcolor('red')
turtle.pendown()
turtle.begin_fill()
turtle.circle(BULLSEYE_RADIUS)
turtle.end_fill()

#Draw the target
turtle.hideturtle()
turtle.speed(0)
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

#Center the turtle
turtle.goto(0,0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

#Get the amount of force to throw the dart
print('Welcome to the game of darts.')
print('How many feet away from the target are you standing?')
distance = int(input('Minimum = 6, maximum = 12: '))
print('How much force will you use to throw the dart?')
force = int(input('Minimum = 1, maximum = 50: '))
angle = float(input("Enter the launch force (1-19): "))

#Calculate the distance
distance = force * FORCE_FACTOR

#Set the heading
turtle.setheading(angle)

#Launch the projectile
turtle.pendown()
turtle.forward(distance)

if (turtle.xcor() >= TARGET_LLEFT_X and
turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
turtle.ycor() >= TARGET_LLEFT_Y and
turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
    print('TARGET HIT!')
else:
    print('You missed the target')




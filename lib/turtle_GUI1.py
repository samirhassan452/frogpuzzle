import turtle
import time
from a_star_algorithm import *
from graph import *
from run_a_star import *

##########################################################
# set up screen
window = turtle.Screen()
# bgcolor == background color
window.bgcolor("lightgreen")
# bgpic == background picture
#window.bgpic("bg.png")
# for frame, to make animation faster
#window.tracer(3)
    

###############################################################
# draw border to prevent object move out of the screen
border = turtle.Turtle()
border.penup()
# now this object in in -300 for x-axis and -300 for y-axis
border.setposition(-250,-250)
# Pull the pen down – drawing when moving, it reverse of penup()
border.pendown()
# to make the size of object = width
border.pensize(3)
# make loop to move on 4 sides ( right, up, left, down )
for side in range(4) :
    border.forward(500)
    # move to 90 degree
    border.left(90)

# to hide object after making 4 sides, after finishing loop
border.hideturtle()

# create multiple pillars
# y lma bnzwed bttl3 le fo2, x bn2ll btrg3 le wara
# fr2 25
# number of goals

#####################################################################
# grog movement after 1 second
list_g = ['A', 'B1', 'C3', 'D4', 'E4', 'F6', 'G6', 'H6', 'I1', 'J1', 'K1', 'L1', 'M1', 'N', 'O', 'P']
maxGoals_frogs = 6
frogs = []

maxGoals_pillars = 7
pillars = []
x_frogs, x_pillars, y = -220, -220, 100    

score = 0
#for i in range(len(path_graph)):
for count in list_g :    
    lists = path_graph[count]
        
    var = y-50
    for count in range(maxGoals_pillars) :
            # add 6 goals in the list
        pillars.append(turtle.Turtle())
        pillars[count].color("blue")
        pillars[count].shape("triangle")
        pillars[count].left(90)
        pillars[count].penup()
        pillars[count].speed(0)
        if count < 3 :
            pillars[count].setposition(x_pillars+20, var)
            x_pillars += 60
        elif count > 3:
            pillars[count].setposition(x_pillars+130, var)
            x_pillars += 60
        else :
            pillars[count].setposition(x_pillars+50, var)
                #x += 30

    y = 100
    x_frogs = -220
    x_pillars = -220
        
    for count_frogs in range(len(lists)) :
        lists[count_frogs].setposition(x_frogs+20, y)
        x_frogs += 70

    score += 1
    border.undo()
    border.penup()
    border.hideturtle()
    border.setposition(-250, 260)
    score_string = "Score: %s" %score
    border.write(score_string, False, align="left", font=("Arial", 15, "normal"))

    time.sleep(1)

    if count == 'P' :
        time.sleep(0.5)




    

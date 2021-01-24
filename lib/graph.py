# update [None] to [ ] to ignore entering in loop
import turtle

available_space = turtle.Turtle()
available_space.penup()
available_space.color("white")
available_space.shape("circle")
    
left_frogs = []
for i in range(3) :
    left_frogs.append(turtle.Turtle())
    left_frogs[i].penup()
    left_frogs[i].color("green")
    left_frogs[i].shape("turtle")

right_frogs = []
for i in range(3) :
    right_frogs.append(turtle.Turtle())
    right_frogs[i].penup()
    right_frogs[i].color("red")
    right_frogs[i].shape("turtle")
'''
path_graph = {
    'A'  : ['Y3', 'Y2', 'Y1', ' ', 'R1', 'R2', 'R3'],
    'B1' : ['Y3', 'Y2', 'Y1', 'R1', ' ', 'R2', 'R3'],
    'C3' : ['Y3', 'Y2', ' ', 'R1', 'Y1', 'R2', 'R3'],
    'D4' : ['Y3', ' ', 'Y2', 'R1', 'Y1', 'R2', 'R3'],
    'E4' : ['Y3', 'R1', 'Y2', ' ', 'Y1', 'R2', 'R3'],
    'F6' : ['Y3', 'R1', 'Y2', 'R2', 'Y1', ' ', 'R3'],
    'G6' : ['Y3', 'R1', 'Y2', 'R2', 'Y1', 'R3', ' '],
    'H6' : ['Y3', 'R1', 'Y2', 'R2', ' ', 'R3', 'Y1'],
    'I1' : ['Y3', 'R1', ' ', 'R2', 'Y2', 'R3', 'Y1'],
    'J1' : [' ', 'R1', 'Y3', 'R2', 'Y2', 'R3', 'Y1'],
    'K1' : ['R1', ' ', 'Y3', 'R2', 'Y2', 'R3', 'Y1'],
    'L1' : ['R1', 'R2', 'Y3', ' ', 'Y2', 'R3', 'Y1'],
    'M1' : ['R1', 'R2', 'Y3', 'R3', 'Y2', ' ', 'Y1'],
    'N'  : ['R1', 'R2', 'Y3', 'R3', ' ', 'Y2', 'Y1'],
    'O'  : ['R1', 'R2', ' ', 'R3', 'Y3', 'Y2', 'Y1'],
    'P'  : ['R1', 'R2', 'R3', ' ', 'Y3', 'Y2', 'Y1']
    }

#print (left_frogs)
'''

path_graph = {
    'A'  : [left_frogs[0], left_frogs[1], left_frogs[2], available_space, right_frogs[2], right_frogs[1], right_frogs[0]],
    'B1' : [left_frogs[0], left_frogs[1], left_frogs[2], right_frogs[2], available_space, right_frogs[1], right_frogs[0]],
    'C3' : [left_frogs[0], left_frogs[1], available_space, right_frogs[2], left_frogs[2], right_frogs[1], right_frogs[0]],
    'D4' : [left_frogs[0], available_space, left_frogs[1], right_frogs[2], left_frogs[2], right_frogs[1], right_frogs[0]],
    'E4' : [left_frogs[0], right_frogs[2], left_frogs[1], available_space, left_frogs[2], right_frogs[1], right_frogs[0]],
    'F6' : [left_frogs[0], right_frogs[2], left_frogs[1], right_frogs[1], left_frogs[2], available_space, right_frogs[0]],
    'G6' : [left_frogs[0], right_frogs[2], left_frogs[1], right_frogs[1], left_frogs[2], right_frogs[0], available_space],
    'H6' : [left_frogs[0], right_frogs[2], left_frogs[1], right_frogs[1], available_space, right_frogs[0], left_frogs[2]],
    'I1' : [left_frogs[0], right_frogs[2], available_space, right_frogs[1], left_frogs[1], right_frogs[0], left_frogs[2]],
    'J1' : [available_space, right_frogs[2], left_frogs[0], right_frogs[1], left_frogs[1], right_frogs[0], left_frogs[2]],
    'K1' : [right_frogs[2], available_space, left_frogs[0], right_frogs[1], left_frogs[1], right_frogs[0], left_frogs[2]],
    'L1' : [right_frogs[2], right_frogs[1], left_frogs[0], available_space, left_frogs[1], right_frogs[0], left_frogs[2]],
    'M1' : [right_frogs[2], right_frogs[1], left_frogs[0], right_frogs[0], left_frogs[1], available_space, left_frogs[2]],
    'N'  : [right_frogs[2], right_frogs[1], left_frogs[0], right_frogs[0], available_space, left_frogs[1], left_frogs[2]],
    'O'  : [right_frogs[2], right_frogs[1], available_space, right_frogs[0], left_frogs[0], left_frogs[1], left_frogs[2]],
    'P'  : [right_frogs[2], right_frogs[1], right_frogs[0], available_space, left_frogs[0], left_frogs[1], left_frogs[2]]
    }

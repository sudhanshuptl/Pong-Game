#Pong game : in Python
#using Online plateform  http://www.codeskulptor.org/
# Sudhanshu Patel
# 5/4/2014
# project still in progress ....

import simplegui
import random

width =600
height = 400
ball_radii = 10
pad_width = 8
pad_height = 80
half_pad_width = pad_width/2
half_pad_height = pad_height/2


#helper function that spawn ball,return position vector & velocity vector
#if right is true spawn to right ,else spawn to left
def ball_init():
    global ball_pos,ball_vel #these are vector stored in list
    ball_pos=[300,200]
    ball_vel=[random.choice([1,-1,2, -2]),random.choice([3,1, -1,0, 2, -2,-3])]
    

def init():
    global paddle1_pos,paddle2_pos,paddle1_vel,paddle2_vel #these are floats 
    global score1,score2 #these are int
    paddle1_pos = [[4, 165], [4, 235]]
    paddle2_pos = [[596, 165], [596, 235]]
    paddle1_vel =3
    paddle2_vel =3
    score1 =0
    score2 =0
    ball_init()
    

def draw(c):
    global score1,score2,paddle1_pos,paddle2_pos,ball_pos,ball_vel
    #update paddle vertical pos & keep paddle on screen
    #update mid line & gutters
    c.draw_line([width/2,0],[width/2,height],1,"White")
    c.draw_line([pad_width,0],[pad_width,height],1,"White")
    c.draw_line([width - pad_width,0],[width - pad_width,height],1,"white")
    
    #draw paddies
    c.draw_polygon(paddle1_pos, 8,"white")
    c.draw_polygon(paddle2_pos, 8,"white")
    #update ball
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
                                          #reflect along x
    if(ball_pos[0] >= 577 or ball_pos[0]<=20):
        ball_vel[0]= - ball_vel[0]   
                                            
    elif(ball_pos[1] <= 15 or ball_pos[1] >= 385 ):
        ball_vel[1] = -ball_vel[1]          #reflect along y
 
    #draw ball & score
    c.draw_circle((ball_pos[0], ball_pos[1]), ball_radii,20,'green')
    
    c.draw_text(str(score1), (150, 50), 24, 'Yellow')
    c.draw_text(str(score2), (450, 50), 24, 'Yellow')
    
def keydown(key):
    global paddle1_vel,paddle2_vel
    if key == simplegui.KEY_MAP["up"] and  paddle2_pos[0][1] >= 0:
        paddle2_pos[0][1] -=paddle2_vel
        paddle2_pos[1][1] -=paddle2_vel
    elif key == key == simplegui.KEY_MAP["down"] and paddle2_pos[1][1] <= 400:
        paddle2_pos[0][1] +=paddle2_vel
        paddle2_pos[1][1] +=paddle2_vel
    
def keyup(key):
    global paddle1_vel,paddle2_vel
    
    
# create Frame
f = simplegui.create_frame("Pong",width,height)
f.set_draw_handler(draw)
f.set_keydown_handler(keydown)
f.set_keyup_handler(keyup)
f.add_button("Restart",init,100)

init()
f.start()
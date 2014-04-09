    #Pong game : in Python
	
	# Sudhanshu Patel
    # 9/4/2014
    
	#Just copy this code & past it to http://www.codeskulptor.org/ and run this code :)
	
    #using Online plateform  http://www.codeskulptor.org/
    # project still in progress ....


import simplegui
import random
import math

#globals 
width =600
height = 400
ball_radii = 10
pad_width = 8
pad_height = 80
half_pad_width = pad_width/2
half_pad_height = pad_height/2
sf=0
#helper function that spawn ball,return position vector & velocity vector
#if right is true spawn to right ,else spawn to left
def start():
    global sf
    sf=1
    init()
def stop():
    global sf
    sf=0

def ball_init():
    global ball_pos,ball_vel #these are vector stored in list
    global paddle1_pos,paddle2_pos
    ball_pos=[300,200]
    ball_vel=[random.choice([-3,3 ]),random.choice([3,-3])]
    paddle1_pos = [[4, 155], [4, 245]]
    paddle2_pos = [[596, 155], [596, 245]]
    
def tick(): #increase velocity by 1 unit after each 3 second 
    global ball_vel
    p = math.sqrt(ball_vel[0]**2 +ball_vel[1]**2)
    p+=0.25
    if(ball_vel[0] >= 0 and ball_vel[1] >=0):  #first cordinate
        o=math.atan(ball_vel[1]/ball_vel[0])
        ball_vel[0]=p*math.cos(o)
        ball_vel[1]=p*math.sin(o)
    elif(ball_vel[0]<=0 and ball_vel[1] >=0): #second cordinate
        o=math.atan(ball_vel[1]/abs(ball_vel[0]))
        ball_vel[0] = -(p*math.cos(o))
        ball_vel[1] = p*math.sin(o)
    elif(ball_vel[0] <=0 and ball_vel[1] <=0): #third cordinate
        o = math.atan(ball_vel[1]/ball_vel[0]) #critical point
        ball_vel[0] = -(p*math.cos(o))
        ball_vel[1] = -(p*math.sin(o))
    elif(ball_vel[0] >=0 and ball_vel[1]<=0): #fourth cordinate
        o=math.atan(abs(ball_vel[1])/ball_vel[0])
        ball_vel[0] = p*math.cos(o)
        ball_vel[1] = -(p*math.sin(o))
        
    
def init():
    global paddle1_vel,paddle2_vel #these are floats 
    global score1,score2 #these are int
    paddle1_vel =0
    paddle2_vel =0
    score1 =0
    score2 =0
    ball_init()
    timer.start()

def draw(c):
    if(sf):
        global score1,score2,paddle1_pos,paddle2_pos,ball_pos,ball_vel
        #update paddle vertical pos & keep paddle on screen
        #update mid line & gutters
        c.draw_line([width/2,0],[width/2,height],1,"White")
        c.draw_line([pad_width,0],[pad_width,height],1,"White")
        c.draw_line([width - pad_width,0],[width - pad_width,height],1,"white")
        
        ###########Logo#############3
        c.draw_text('Jai ', (270, 200), 20, '#FF3300')
        c.draw_text('Hind ', (300, 200), 20, '#FFFFFF')
        c.draw_text('!!', (350, 200), 20, '#00CC00')        
        #####################paddies
                     #paddle 1 movement
        if  paddle1_pos[0][1] >0 and paddle1_pos[1][1] <400 :
            paddle1_pos[0][1] +=paddle1_vel
            paddle1_pos[1][1] +=paddle1_vel
        elif(paddle1_pos[0][1] == 0 and paddle1_vel > 0):
            paddle1_pos[0][1] +=paddle1_vel
            paddle1_pos[1][1] +=paddle1_vel
        elif(paddle1_pos[1][1] == 400 and  paddle1_vel < 0):
            paddle1_pos[0][1] +=paddle1_vel
            paddle1_pos[1][1] +=paddle1_vel
            
        c.draw_polygon(paddle1_pos, 8,"white")#paddle 1 draw 
        
                   #paddle 2 movement
        if  paddle2_pos[0][1] > 0 and paddle2_pos[1][1] < 400 :
            paddle2_pos[0][1] +=paddle2_vel
            paddle2_pos[1][1] +=paddle2_vel
        elif(paddle2_pos[0][1] == 0 and paddle2_vel > 0):
            paddle2_pos[0][1] +=paddle2_vel
            paddle2_pos[1][1] +=paddle2_vel
        elif(paddle2_pos[1][1] == 400 and  paddle2_vel < 0):
            paddle2_pos[0][1] +=paddle2_vel
            paddle2_pos[1][1] +=paddle2_vel
            
        c.draw_polygon(paddle2_pos, 8,"white") #paddle 2 draw 
        
        ########################update ball
        ball_pos[0]+=ball_vel[0]
        ball_pos[1]+=ball_vel[1]
                                              #reflect along x
        if(ball_pos[0]<=20 and  ball_pos[1]>= paddle1_pos[0][1] and ball_pos[1]<= paddle1_pos[1][1]): # for paddle 1
            ball_vel[0]= - ball_vel[0]
        elif(ball_pos[0] <20):
            score2+=1
            ball_init()
        elif(ball_pos[0] >= 577 and ball_pos[1]>= paddle2_pos[0][1] and ball_pos[1]<= paddle2_pos[1][1]): #for paddle 2
            ball_vel[0]= - ball_vel[0]
        elif(ball_pos[0] > 577):
            score1+=1
            ball_init()
            
        elif(ball_pos[1] <= 15 or ball_pos[1] >= 385 ):
            ball_vel[1] = -ball_vel[1]          #reflect along y
     
        #######################draw ball & score
        c.draw_circle((ball_pos[0], ball_pos[1]), ball_radii,15,'green')
        
        c.draw_text(str(score1), (150, 50), 24, 'Yellow')
        c.draw_text(str(score2), (450, 50), 24, 'Yellow')
    else:
       c.draw_text('START GAME', (200, 100), 30, '#00FFFF')
       c.draw_text('Jai ', (250, 300), 30, '#FF3300')
       c.draw_text('Hind ', (290, 300), 30, '#FFFFFF')
       c.draw_text('!!', (360, 300), 30, '#00CC00')
        
def keydown(key):
    global paddle1_vel,paddle2_vel
    if key == simplegui.KEY_MAP["up"]:  #paddle 2
        paddle2_vel = -5       
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 5
    elif key == simplegui.KEY_MAP["w"]: #paddle 1
         paddle1_vel = -5
    elif key == simplegui.KEY_MAP["s"]:
         paddle1_vel = 5
    
def keyup(key):
    global paddle1_vel,paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0
    
# create Frame
f = simplegui.create_frame("Pong",width,height)
f.set_draw_handler(draw)
f.set_keydown_handler(keydown)
f.set_keyup_handler(keyup)
f.add_button("start",start,100)
f.add_button("Restart",stop,100)
timer=simplegui.create_timer(750,tick)
f.start()
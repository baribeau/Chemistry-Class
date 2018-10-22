#   Julia Baribeau
#   April 14, 2017

############################ Inputs ############################
from tkinter import *
from math import *
from time import *
from random import *
############################ Set up screen ############################
myInterface = Tk()
s = Canvas( myInterface, width=800, height=800, background="snow2" )
s.pack()

############################ Background ############################
s.create_rectangle(525,690, 550,805, fill = "gray12")
s.create_rectangle(550,690, 568,805, fill = "gray8")
s.create_rectangle(717,580, 742,801, fill = "gray12")
s.create_rectangle(742,580, 760,805, fill = "gray8")
s.create_polygon(-200,700, 25,570, 760,570, 550,700, -5,700, fill = "grey20", width = 1, outline = "black")
s.create_polygon(760,570, 760,600, 550,730, 550,700, fill = "gray10", width = 1, outline = "black")
s.create_rectangle(-5,700, 550,730, fill = "gray15")
s.create_rectangle(40,60, 240,175, fill = "deepskyblue4")
for texture in range(0,2000):
    x1 = randint(42,238)
    y1 = randint(62,173)
    x2 = x1+1
    y2 = y1+1
    s.create_oval(x1,y1, x2,y2, fill = "deepskyblue3", outline = "deepskyblue3")
s.create_text(140,98, fill = "white",font = "helvetica 13", text = "CAREFUL OF SPILLS")
s.create_line(50,118, 230,118, fill = "white", width = 2)
s.create_text(140,138, fill = "white",font = "helvetica 13", text = "IT'S RARELY WATER")

poster = PhotoImage(file = "poster.gif")
s.create_image(602,150, image = poster)

s.create_rectangle(750,25, 780,42, fill = "white", outline = "white")
x = 750
while x < 780:
    gap = uniform(0,2)
    width = uniform(0,1)
    s.create_line(x,25, x,42, width = width, fill= "black")
    x += gap

s.create_rectangle(140,480, 245,640, fill = "", width = 3)

############################ Pouring Sequence ############################
x1Pour = 240
y1Pour = 325
deltaThetaPour = 0.01745
widthPour = 160
heightPour = 90
diagPour = sqrt(widthPour**2+heightPour**2)

waterPouring = s.create_rectangle(240,280, 400,325, fill = "blue", outline = "")

y1Rise = 640

for i in range(89):
    thetaPour = i*deltaThetaPour
    
    x2 = x1Pour+widthPour*cos(thetaPour)
    y2 = y1Pour-widthPour*sin(thetaPour)
    x3 = x1Pour+diagPour*cos(thetaPour+0.51)
    y3 = y1Pour-diagPour*sin(thetaPour+0.51)
    x4 = x1Pour+heightPour*cos(thetaPour+pi/2)
    y4 = y1Pour-heightPour*sin(thetaPour+pi/2)
    if i < 54:
        xT = x1Pour+heightPour/2*cos(thetaPour+pi/2)
        yT = y1Pour-heightPour/2*sin(thetaPour+pi/2)
    else:
        xT += 1
        yT += 1

    y1Rise = y1Rise-0.9

    waterSupp = s.create_polygon(240,325, 240,280, xT,yT, fill = "blue")
    fall = s.create_polygon(x1Pour,y1Pour, x1Pour,637, xT,637, xT,yT, fill = "blue", outline = "")
    flow = []
    x = []
    y = []
    length = []
    for a in range(20):
        flow.append(0)
        x.append(uniform(x1Pour,xT))
        y.append(uniform(y1Pour,617))
        length.append(randint(4,10))
    for a in range(20):
        flow[a] = s.create_line(x[a],y[a], x[a],y[a]+length[a], fill = "lightblue")
    eraser = s.create_polygon(x1Pour,y1Pour, x2,y2, 402,y2, 400,325, fill = "snow2")
    pour = s.create_polygon(x1Pour,y1Pour, x2,y2, x3,y3, x4,y4, fill = "", outline = "black", width = 3)
    water = s.create_rectangle(140,y1Rise, 245,640, fill = "blue", outline = "blue")
    s.create_rectangle(140,480, 245,640, fill = "", width = 3)

    s.update()
    sleep(0.08)
    for a in range(20):
        s.delete(flow[a])
    if i < 88:
        s.delete(pour, waterSupp, fall, water)
    if i == 88:
        s.delete(waterSupp, fall, waterPouring, eraser, pour)

############################ Goodbye Empty Beaker ############################
while x1Pour < 804:
    x1Pour += 13
    y1Pour += 0.5
    x2 += 13
    y2 += 0.5
    x3 += 13
    y3 += 0.5    
    x4 += 13
    y4 += 0.5

    pour2 = s.create_polygon(x1Pour,y1Pour, x2,y2, x3,y3, x4,y4, fill = "", width = 3, outline = "black")

    s.update()
    sleep(0.03)
    s.delete(pour2)

############################ Hello Reactive Metal ############################
y1Rock = 360
for f in range(36):
    x1Rock = f*5
    x2Rock = x1Rock+10
    y2Rock = y1Rock+10
    rock = s.create_oval(x1Rock,y1Rock, x2Rock,y2Rock, fill = "gray50")
    s.update()
    sleep(0.03)
    s.delete(rock)

############################ Drop Metal Into Water ############################
for f in range(52):
    if y2Rock < 610:
        y1Rock = 360 + 5*f + 0.5*f**2
        y2Rock = y1Rock+10
        rock = s.create_oval(x1Rock,y1Rock,x2Rock,y2Rock, fill = "gray50")
        s.update()
        sleep(0.03)
        s.delete(rock)

############################ Filling Arrays ############################
### For water droplets inside beaker ###
drops = 800
xDrops = []
yDrops = []
yStart = []
dSizes = []
dSpeeds = []
dropImages = []
t = []
for i in range(drops):
    xDrops.append(uniform(142,238))
    yStart.append(uniform(560,630))
    yDrops.append(590)
    dSizes.append(randint(1,5))
    dSpeeds.append(uniform(1,15))
    dropImages.append(0)
    t.append(0)

### For water droplets that fly out of beaker ###
xStartOut = []
yStartOut = []
xOut = []
yOut = []
rOutDrops = []
rOutSpeeds = []
angles = []
dOutImages = []
tOut = []
gravVar = []
colours = ["blue", "blue", "lightblue"]
for i in range(drops):
    xStartOut.append(uniform(142,238))
    yStartOut.append(uniform(483,477))
    xOut.append(xStartOut[i])
    yOut.append(yStartOut[i])
    rOutDrops.append(0)
    rOutSpeeds.append(uniform(1,5))
    angles.append(uniform(0.7,pi-1))
    dOutImages.append(0)
    tOut.append(1)
    gravVar.append(0)

mod = pi

############################ Explosive Reaction ############################
for f in range(120):

    ### Water droplets ###
    for i in range(drops):            
        if y1Rise<630:
            b = randint(0,2)
            colour = colours[b]
            dropImages[i] = s.create_oval(xDrops[i],yDrops[i], xDrops[i]+dSizes[i],yDrops[i]+dSizes[i], fill = colour, outline = "")
            yDrops[i] = yStart[i]-dSpeeds[i]*t[i]
            t[i] = t[i]+1

            if yDrops[i]<480:
                t[i] = 0
                yDrops[i] = yStart[i]

        if f>5:
            if angles[i]>pi/2 and angles[i]<3*pi/2:
                gravVar[i] -= 0.05
                argument = angles[i]*(1-gravVar[i])#%mod
                if argument > 5*pi/4:
                    argument = 5*pi/4
                #mod = 5*pi/4
                
            else:
                if angles[i]<pi/2:
                    gravVar[i] += 0.05
                    argument = angles[i]*(1-gravVar[i])
                    if argument < 0:
                        argument = 2*pi + argument
                        
            b = randint(0,2)
            colour = colours[b]    
            xOut[i] = xStartOut[i]+rOutDrops[i]*cos(angles[i])*tOut[i]
            yOut[i] = yStartOut[i]-rOutDrops[i]*sin(argument)*tOut[i]#+0.3*tOut[i]**2
            dOutImages[i] = s.create_oval(xOut[i],yOut[i], xOut[i]+dSizes[i],yOut[i]+dSizes[i], fill = colour, outline = "")
            rOutDrops[i] += rOutSpeeds[i]#*tOut[i]
            tOut[i] += 1

            if y1Rise<630:
                if 0>=yOut[i] or 800<=yOut[i] or 0>=xOut[i] or 800<=xOut[i]:
                    tOut[i] = 1
                    rOutDrops[i] = 0
                    gravVar[i] = 0

    ### Fizzing metal ###
    if y1Rise<630:
        x1 = randint(-10,-1)
        y1 = randint(-2,2)
        x2 = randint(-10,-1)
        y2 = randint(-8,-1)
        x3 = randint(1,8)
        y3 = randint(-10,-1)
        x4 = randint(1,9)
        y4 = randint(1,10)
        x5 = randint(-7,5)
        y5 = randint(1,8)

        y1Rise += 0.8
        s.delete(water)
        water = s.create_rectangle(142,y1Rise, 243,638, fill = "blue", outline = "blue")

        flow = []
        x = []
        y = []
        length = []
        for a in range(20):
            flow.append(0)
            x.append(uniform(142,233))
            y.append(uniform(y1Rise,638))
            length.append(randint(4,10))
        for a in range(20):
            flow[a] = s.create_line(x[a],y[a], x[a]+length[a],y[a], fill = "lightblue")

        rock = s.create_polygon(180+x1,630+y1, 180+x2,630+y2, 180+x3,630+y3, 180+x4,630+y4, 180+x5,630+y5, fill = "gray50", smooth = True)

    s.update()
    sleep(0.1)
    for a in range(20):
        s.delete(flow[a])
    if y1Rise<629:
        s.delete(rock)
    for i in range(drops):
        s.delete(dropImages[i], dOutImages[i])




######################### Grid Tool for Development #########################

##spacing = 30
##for xAxis in range(0, 800, spacing): 
##    s.create_line(xAxis,30, xAxis,800, fill="gray50")
##    s.create_text(xAxis,10, text=str(xAxis), font="Comic 8", anchor = N, fill = "red3")
##
##for yAxis in range(0,800, spacing):
##    s.create_line(30,yAxis, 800,yAxis, fill="gray50")
##    s.create_text(10,yAxis, text=str(yAxis), font="Comic 8", anchor = W, fill = "red3")

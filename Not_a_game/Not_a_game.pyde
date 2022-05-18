from cat import *
from platforma import *
from kamenn import *
from drevo import *
import time
q=0
w=0
kam=0
der=0
x=600
y=423
def setup():
    global q, w, kam, der
    size(1400, 710)
    q=loadImage('cat2.png')
    w=loadImage('platforma.png')
    kam=loadImage('kamen.png')
    der=loadImage('derevoNORM-removebg-preview.png')
def draw():
    background(255)
    global q,x,y,w,e,kam,der
    catcat(q, x, y)
    plat(w)
    kamen(kam)
    derevo(der)
    if keyPressed == False:
        if y<423:
            y=y+5
def keyPressed():
    global y
    if key == CODED:
        if keyCode == UP:
            if y>323:
                y=y-150

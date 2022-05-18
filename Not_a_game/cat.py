from platforma import *
def catcat(q, x, y):
    global x1,y1
    image(q, x, y, 100, 110)
    if x >= 1300:
        x = 1298
    if x <= 0:
        x = 1

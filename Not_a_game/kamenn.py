xk = 1400
def kamen(kam, x, y):
    global xk
    image(kam, xk, 450, 100, 110)
    xk=xk-7
    if xk<=-250:
        xk=random(1500, 1800)
    if x +80 >= xk and x<=xk+100 and y+110>=450 and y<=450+110:
        exit()
        rect(0, 0, 1400, 710)

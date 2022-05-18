xd = 2100
def derevo(x , y, der):
    global xd
    image(der, xd, 400, 200, 150)
    xd=xd-7
    if xd<=-250:
        xd=random(2000, 2400)
    if x + 60 >= xd and x<=xd+200 and y+110>=400 and y<=400+150:
        exit()
        rect(0, 0, 1400, 710)

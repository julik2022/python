xd = 2100
def derevo(der):
    global xd
    image(der, xd, 285, 350, 250)
    xd=xd-7
    if xd<=-250:
        xd=random(2000, 2400)

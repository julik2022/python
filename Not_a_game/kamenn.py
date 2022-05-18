xk = 1400
def kamen(kam):
    global xk
    image(kam, xk, 450, 100, 110)
    xk=xk-7
    if xk<=-250:
        xk=random(1500, 1800)

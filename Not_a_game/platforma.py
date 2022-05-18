x1=-200
def plat(w):
    global x1,y1
    image(w, x1, 530, 2000, 400)
    x1 = x1 - 7
    if x1 <= -600:
        x1=-200
        

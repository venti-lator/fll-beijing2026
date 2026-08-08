from Base import *

def Run(): #1 : 1.5
    
    forward(0, 720, 50, 70, 20, 500, 1)
    right_att(15, 160)
    forward(0, 50, 20, 20, 20, 80, 1)
    right_att(-100, 1800)
    backward(0, 100, 20, 20, 20, 500, 0.2)
    LQR_pivot(55, direction=left)
    forward(0, 600, 50, 70, 20, 500, 1)#skibiditoilet
    right_att(-15, 250, is_wait=False)
    LQR_pivot(40, direction=left)
    forward(0, 190, 30, 30, 30, 500, 1)
    wait(300)
    left_att(100, 250)
    left_att(-100, 400)
    backward(0, 200, 40, 40, 40, 500, 0.2)
    LQR_povorot(-73)
    Curve(1600, -41, speed=900)
    
    # forward(0, 3000, 70, 100, 100, 500, 3)

print(str(hub.battery.voltage()))
# Run()
from Base import *

def Run(): #1 : 1.5
    print(str(hub.battery.voltage()))
    forward(0, 1270, 50, 70, 40, 800, 1)
    right_att(100, 100)
    LQR_pivot(-39, direction=left)
    forward(0, 120, 50, 70, 50, 500, 1)
    right_att(70, -110)
    forward(0, 160, 30, 30, 30, 500, 1)
    # wait(200)
    right_att(70, 1000)
    backward(0, 240, 50, 50, 50, 500, 0.5)
    LQR_pivot(45, direction=left)
    backward(0, 215, 50, 50, 50, 500, 0.5)
    # left_att(35, -110)
    wait(600)
    left_att(30, 800)
    backward(0, 1100, 70, 70, 70, 500, 0.9)



# Run()
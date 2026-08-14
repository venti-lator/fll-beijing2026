from Base import *

def Run(): #1 : 1.5
    print(str(hub.battery.voltage()))
    left_att(100, -200)
    LQR_pivot(57)
    right_att(40, -260)
    forward(0, 885, 50, 80, 30, 650, 2)
    left_att(100, 300)
    LQR_pivot(-22, direction=left)
    left_att(100, -400)
    LQR_povorot(41, max_power=30)
    forward(0, 300, 40, 70, 40, 150, 2)
    LQR_pivot(-48, direction=left)
    forward(0, 840, 40, 70, 40, 750, 2)
    right_att(40, 300)
    backward(0, 70, 40, 40, 40, 50, 0.5)
    LQR_pivot(33, direction=left)
    backward(0, 440, 40, 40, 40, 380, 1)
    right_att(100, 450)
    forward(0, 200, 40, 70, 40, 150, 1)




# Run()

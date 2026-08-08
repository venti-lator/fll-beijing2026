from Base import *

def Run(): #1 : 1.5
    print(str(hub.battery.voltage()))
    left_att(100, -400)
    LQR_pivot(57)
    right_att(40, -250)
    forward(0, 800, 40, 70, 40, 700, 2)
    left_att(100, 300)
    LQR_pivot(-25, direction=left)
    left_att(100, -400)
    LQR_povorot(40)
    forward(0, 300, 40, 70, 40, 150, 2)
    LQR_pivot(-38, direction=left)
    forward(0, 860, 40, 70, 40, 750, 2)
    right_att(40, 300)
    backward(0, 70, 40, 40, 40, 70, 2)
    LQR_pivot(30, direction=left)
    backward(0, 450, 40, 40, 40, 450, 2)
    right_att(100, 450)
    forward(0, 200, 40, 70, 40, 150, 2)




# Run()
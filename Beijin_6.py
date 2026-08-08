from Base import *

def Run(): #1 : 1.5
    print(str(hub.battery.voltage()))
    # PidDrive(10)
    forward(0, 1230, 20, 60, 40, 950, 2)
    LQR_pivot(43)
    right_att(100, -700)
    forward(0, 220, 30, 30, 30, 70, 2)
    left_att(100, 450)
    right_att(100, 650)
    LQR_pivot(47, direction=left)
    left_att(10, 400, is_wait=False)
    backward(0, 300, 50, 50, 50, 200, 1)
    left_att(-100, 400)
    LQR_pivot(60)
    forward(0, 1210, 40, 70, 70, 1000, 2)



# Run()
from Base import *

def Run(): #1 : 1.5
    print(str(hub.battery.voltage()))
    # PidDrive(10)
    forward(0, 1230, 40, 80, 40, 950, 2)
    LQR_pivot(43)
    right_att(100, -700)
    forward(0, 150, 30, 30, 30, 100, 0.2)
    move_time(30, 30, 300)
    left_att(100, 450)
    right_att(100, 650)
    LQR_pivot(47, direction=left)
    left_att(100, 500, is_wait=False)
    backward(0, 300, 50, 50, 50, 200, 1)
    left_att(-100, 400)
    LQR_pivot(60)
    forward(0, 1210, 40, 100, 100, 1000, 2)



# Run()

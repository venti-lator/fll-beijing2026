from Base import *

def Run(): #1 : 1.5
    print(str(hub.battery.voltage()))
    right_att(100, -250, is_wait=False)
    left_att(100, -30)
    forward(0, 680, 50, 60, 40, 500, 1)
    right_att(100, -4300)
    backward(0, 120, 30, 30, 30, 150, 1)
    LQR_pivot(-43)
    forward(0, 595, 50, 60, 60, 500, 1)
    left_att(100, 200)
    left_att(50, 100, is_wait=False)
    # backward(0, 120, 30, 30, 30, 120, 0.2)
    move_time(-40, -40, 600)
    left_att(-100, 310)
    backward(0, 800, 100, 100, 100, 800, 1.5)



# Run()
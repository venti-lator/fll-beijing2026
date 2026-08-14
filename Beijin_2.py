from Base import *

def Run(): #1 : 1.5
    print(str(hub.battery.voltage()))
    forward(0, 1230, 50, 80, 40, 950, 2)
    wait(200)
    LQR_povorot(180)
    right_att(100, -500)
    backward(0, 530, 50, 50, 50, 500, 0.5)
    LQR_povorot(-90)
    wait(100)
    forward(0, 255, 35, 35, 35, 200, 0.5)
    left_att(100, 950)
    right_att(40, 400)
    PidDrive(-200, speed=800)
    LQR_pivot(110, max_power=100, k1 = 8, k2=0.6, tolerance=1)
    forward(0, 1500, 100, 100, 100, 1200, 2)


# Run()

from Base import *

def Run(): #1 : 1.5
    
    forward(0, 720, 50, 70, 20, 500, 1)
    right_att(20, 200)
    # forward(0, 50, 20, 20, 20, 80, 1)
    move_time(40, 40, 200)
    right_att(-100, 1200)
    backward(0, 100, 30, 30, 30, 90, 0.2)
    LQR_pivot(55, direction=left)
    forward(0, 600, 50, 70, 20, 500, 1)#skibiditoilet
    right_att(-15, 250, is_wait=False)
    LQR_pivot(40, direction=left)
    forward(0, 100, 50, 50, 30, 150, 1)
    move_time(60, 60, 150)
    wait(100)
    move_time(-20, -20, 200)
    left_att(100, 400)
    wait(100)
    left_att(-100, 500)
    backward(0, 200, 60, 60, 60, 500, 0.2)
    LQR_povorot(-67)
    Curve(2100, -33, speed=900)
    


print(str(hub.battery.voltage()))
# Run()

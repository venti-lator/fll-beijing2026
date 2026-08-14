from Base import *

def Run(): #1 : 1.5
    print(str(hub.battery.voltage()))
    # PidDrive(10)
    wait(400)
    forward(0, 300, 20, 60, 65, 1000, 2)
    LQR_pivot(38, max_power=50)
    forward(0, 320, 20, 60, 60, 1000, 2)
    wait(500)
    backward(0, 680, 70, 70, 70, 510, 2)
    LQR_povorot(-40)

# Run()

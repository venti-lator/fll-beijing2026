from Base import *

def Run(): #1 : 1.5
    print(str(hub.battery.voltage()))
    forward(0, 1000, 70, 70, 50, 800, 2)
    # wait(300)
    leftAttachmentMotor.run_time(500, 400)
    move_deg(-95, -100, 1000)

# Run()

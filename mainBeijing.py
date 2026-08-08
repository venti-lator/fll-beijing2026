from pybricks.hubs import PrimeHub
from pybricks.parameters import Button
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase

import Beijin_1
import Beijin_2
import Beijin_3
import Beijin_4
import Beijin_5
import Beijin_6
import Beijin_7
import Beijin_8

hub = PrimeHub()

run_counts = 9

hub.system.set_stop_button(Button.CENTER)

#Displays battery on the screen
def summon_battery():
    for i in range (0,5):
        for j in range (0, 5):
            hub.display.pixel(i, j, brightness=0)


    hub.display.pixel(0,2)
    hub.display.pixel(1,1)
    hub.display.pixel(1,2)
    hub.display.pixel(1,3)
    hub.display.pixel(2,1)
    hub.display.pixel(2,3)
    hub.display.pixel(3,1)
    hub.display.pixel(3,3)
    hub.display.pixel(4,1)
    hub.display.pixel(4,2)
    hub.display.pixel(4,3)#skibidi toilet
#skibiditoilet
    #skibiditoilet
    #skibiditoilet
    
#For every index chooses a run
def Choice(index):
    if index == 1:        #Run 1
        Beijin_6.Run()
    elif index == 2:      #Run 2
        Beijin_3.Run()
    elif index == 3:      #Run 3
        Beijin_5.Run()
    elif index == 4:      #Run 4
        Beijin_4.Run()
    elif index == 5:
        Beijin_2.Run()
    elif index == 6:
        Beijin_7.Run()
    elif index == 7:
        Beijin_1.Run()
    elif index == 8:
        Beijin_8.Run()
    elif index == 9:      #Battery
        hub.display.text(str(int(hub.battery.voltage()))) #8277
        wait(500)
        summon_battery()
        
#Main
def Control():
    index = 1
    hub.display.number(index)
    while True:
        #Getting all the pressed buttons
        pressed = hub.buttons.pressed()

        
        if Button.BLUETOOTH in pressed:         #Running the index
            while (Button.BLUETOOTH in pressed):
                pressed = hub.buttons.pressed()
            wait(40)
            Choice(index)

        
        elif Button.LEFT in pressed:        #Decreasing the index
            if index > 1:        #Decrease
                index -= 1
            else:
                index = run_counts
            
            if index != run_counts:         #Choosing what to display
                hub.display.number(index)
            else:
                summon_battery()
            
            while (Button.LEFT in pressed):         #Waiting until LEFT is released
                pressed = hub.buttons.pressed()
            wait(40)

        #Increasing the index
        elif Button.RIGHT in pressed:
            if index < run_counts:      #Increase
                index += 1
            else:
                index = 1
      
            if index != run_counts:         #Choosing what to display
                hub.display.number(index)
            else:
                summon_battery()
  
            while (Button.RIGHT in pressed):        #Waiting until RIGHT is released
                pressed = hub.buttons.pressed()
            wait(40)

        #print("current: " + str(br.hub.battery.current()))
        #print("voltage: " + str(br.hub.battery.voltage()))
        wait(10)

Control()
from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
me.get_battery()

me.move_forward(30)

# Basic Takeoff movement && Landing
me.land()
me.send_rc_control(0, 50, 0, 0)
sleep(2)
me.send_rc_control(0,0,0,50)
me.land()
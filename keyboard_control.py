import KeyPressModule as kp
from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()

kp.init()

while True:
    if kp.getKey("w"): me.send_rc_control(0, 50, 0, 0)
    elif kp.getKey("s"): me.send_rc_control(0, -50, 0, 0)
    elif kp.getKey("a"): me.send_rc_control(50, 0, 0, 0)
    elif kp.getKey("d"): me.send_rc_control(-50, 0, 0, 0)

    if kp.getKey("UP"): me.send_rc_control(0, 0, 50, 0)
    elif kp.getKey("s"): me.send_rc_control(0, 0, -50, 0)
    elif kp.getKey("a"): me.send_rc_control(0, 0, 0, 50)
    elif kp.getKey("d"): me.send_rc_control(0, 0, 0, -50)

    elif kp.getKey("t"): me.takeoff()
    elif kp.getKey("l"): me.land()

    else: print("No input detected")
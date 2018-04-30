import numpy as np
import sys
import time
import Constants
from gpiozero import PWMOutputDevice

class Motor(Object):

    def __init__(self, pins):
        fwdpin = pins[0]
        revpin = pins[1]
        pwmpin = pins[2]

        self.pwm = PWMOutputDevice(pwmpin, True, 0 , 1000)
        self.fwd = PWMOutputDevice(fwdpin)
        self.rev = PWMOutputDevice(revpin)

        self.speed = 0

    def stop(self):
        fwd.value = False
        rev.value = False
        pwm.value = 0

    def setMotor(self, speed):
        if speed > 0.0:
            fwd.value = True
            rev.value = False
            pwm.value = np.absolute(speed)
        elif speed < 0.0:
            fwd.value = False
            rev.value = True
            pwm.value = np.absolute(speed)
        else:
            stop()

    #speed is a value between -1 and 1
    #rotation is a value between -1 and 1: - is left, + is right
    def drive(self, speed, rotation, squaredInputs=False):
        if squaredInputs:
            speed *= speed
            rotation *= rotation

        if speed > 0.0:
            if rotation > 0.0:

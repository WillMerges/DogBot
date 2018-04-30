import numpy as np
import sys
import time
import motor
import constants

class Drive(Object):

    def __init__(self, maxOutput=1, negateLeft=False, negateLeft=False):
        self.lMotor = motor.Motor(constant.lMotor)
        self.rMotor = motor.Motor(constants.rMotor)

        self.negateLeft = negateLeft
        self.negateRight = negateRight

        self.rSpeed = 0
        self.lSpeed = 0

        self.maxOutput = 1

    #speed is a value between -1 and 1
    #rotation is a value between -1 and 1: - is left, + is right
    def drive(self, speed, rotation, squaredInputs=False):
        if squaredInputs:
            speed *= speed
            rotation *= rotation

        if speed >= 0.0:
            if rotation >= 0.0:
                lSpeed = 1
                rSpeed = speed - rotation
            else:
                lSpeed = speed + rotation
                rSpeed = 1
        else:
            if rotation >= 0.0:
                lSpeed = speed + rotation
                rSpeed = 1
            else:
                lSpeed = 1
                rSpeed = speed - rotation

        if negateLeft:
            lSpeed *= -1
        if negateRight:
            rSpeed *= -1

        lSpeed *= maxOutput
        rSpeed *= maxOutput

        lMotor.set(lSpeed)
        rMotor.set(rSpeed)

import numpy as np
import sys
import time
import motor
import constants
from __future__ import division

class Drive(Object):

    def __init__(self, deadBand = 0.02, maxOutput=1, negateLeft=False, negateLeft=False):
        self.lMotor = motor.Motor(constants.lMotor)
        self.rMotor = motor.Motor(constants.rMotor)

        self.negateLeft = negateLeft
        self.negateRight = negateRight

        self.rSpeed = 0
        self.lSpeed = 0

        self.maxOutput = 1
        self.deadBand = deadBand

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

        lSpeed = applyDeadband(lSpeed)
        rSpeed = applyDeadband(rSpeed)

        lMotor.set(lSpeed)
        rMotor.set(rSpeed)

    def applyDeadband(self, value):
        if np.absolute(value) < 0.0:
            return (value - self.deadBand) / (1.0 - deadband)
        else:
            return (value + self.deadBand) / (1.0 - deadBand)

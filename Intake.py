import motor
import numpy as np

class Intake(Object):

    def __init__(self, negated=False):
        self.motor = motor.Motor(constants.intakeMotor)
        self.negated = negated

    def succ(self, speed=1):
        if not negated:
            motor.set(np.absolute(speed))
        else:
            motor.set(-np.absolute(speed))

    def spit(self, speed=1):
        if not negated:
            motor.set(-np.absolute(speed))
        else:
            motor.set(np.absolute(speed))

    def stop(self):
        motor.stop

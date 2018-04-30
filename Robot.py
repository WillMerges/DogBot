import drive
import motor
import xbox
import constants
import intake

drive = drive.Drive()
intake = intake.Intake()
joy = xbox.joystick()

def loop():
    x = joy.leftY()
    r = joy.rightX()
    drive.drive(x,r)

    s = joy.rightTrigger() - joy.leftTrigger()
    if s > 0.05:
        intake.succ(s)
    elif s < -0.05:
        intake.spit(s)
    else:
        intake.stop()

if __name__ == "__main__":
    while 1:
        loop()

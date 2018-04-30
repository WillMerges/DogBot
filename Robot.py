import drive
import motor
import xbox
import constants

drive = drive.Drive()
joy = xbox.joystick

def loop():
    x = joy.leftX()
    r = joy.rightX()
    drive.drive(x,r)


if __name__ == "__main__":
    while 1:
        loop()

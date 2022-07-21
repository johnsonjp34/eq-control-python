# sudo pip3 install adafruit-circuitpython-motorkit
import time
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

kit = MotorKit()

#Basic Stepper Motor Control.
#Activates a step forward or backwards a given number of steps.
#az/alt tied to the separate motors.
#If single motor used alt axis, you must move the alt all the way down first.

def stepforward(n,whichMotor):
    steps = round(n)
    for i in range(steps):
        if whichMotor == "az":
            kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        if whichMotor == "alt":
            kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        time.sleeo(0.01)



def stepbackward(n,whichMotor):
    steps = round(n)
    for i in range(steps):
        if whichMotor == "az":
            kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        if whichMotor == "alt":
            kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        time.sleep(0.01)

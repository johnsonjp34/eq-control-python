#sudo pip3 install adafruit-circuitpython-motorkit
import time
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

kit = MotorKit()

def stepforward():
    for i in range(1000):
        kit.stepper1.onestep(direction=stepper.FORWARD,style=stepper.DOUBLE)
        # kit.stepper2.onestep(direction="stepper.BACKWARD")
        time.sleep(0.01)

def stepbackward():
    for i in range(1000):
        kit.stepper1.onestep(direction=stepper.BACKWARD,style=stepper.DOUBLE)
        # kit.stepper2.onestep(direction="stepper.BACKWARD")
        time.sleep(0.01)


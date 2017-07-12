from __future__ import print_function
from __future__ import division
from builtins import input
##The above lines are random crap
import time
from BrickPi import *

BrickPiSetup()

BrickPi.MotorEnable[PORT_A] = 1 #heading rotator
BrickPi.MotorEnable[PORT_B] = 1 #angle rotator
BrickPi.MotorEnable[PORT_C] = 1 #angle rotator
BrickPi.SensorType[PORT_1] = TYPE_SENSOR_TOUCH

BrickPiSetupSensors()

power = 150 #calibrated for "power = 150"
            #Set to 150 if not 150
th = 1 #This value is equal to seconds it takes to turn one degree for the heading
ta = 1 #This value is equal to seconds it takes to turn one degree for the angle

def Control (h, a):
    while True:
        BrickPiUpdateValues()
        ot = time.time()
        print('Set Heading')
        while(time.time() - ot < th * h):
            BrickPiUpdateValues()
            BrickPi.MotorSpeed[PORT_A] = power
        time.sleep(1)
        BrickPi.MotorSpeed[PORT_A] = 0
        ot = time.time()
        print('Set Angle')
        while(time.time() - ot < ta*a):
            BrickPiUpdateValues()
            BrickPi.MotorSpeed[PORT_B] = power
            BrickPi.MotorSpeed[PORT_C] = power
        BrickPi.MotorSpeed[PORT_B] = 0
        BrickPi.MotorSpeed[PORT_C] = 0
        break
x = 5
y = 5
MotorControl(x, y)

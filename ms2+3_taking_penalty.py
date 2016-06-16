import pyb
from pyb import *
from pyb import Pin, ADC, Timer

print('Bluetooth testing')
print('Initialising taking_penalty')

# Key variables --------------------------------------------------
speed = 50 # standard driving speed


# Defining the motor modules and servo--------------------------------------
A1 = Pin('Y9',Pin.OUT_PP) # motor A is on the RHS of the vehicle
A2 = Pin('Y10',Pin.OUT_PP)
motor1 = Pin('X1')

B1 = Pin('Y11',Pin.OUT_PP) # motor B is on the LHS of the vehicle
B2 = Pin('Y12',Pin.OUT_PP)
motor2 = Pin('X2')

tim = Timer(2, freq = 1000)
ch1 = tim.channel(1, Timer.PWM, pin = motor1)
ch2 = tim.channel(2, Timer.PWM, pin = motor2)

servo = Servo(3) # servo on position 3 (X3, VIN, GND)

# Defining servo function (To be placed under 'Defining Button Functions') --------------------------
def servoswing():
    servo.angle(90) # move to the release position
    pyb.delay(500)
    servo.angle(-45, 1000) # move to ready position in 1000 milisecs
    pyb.delay(500)
    



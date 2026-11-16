from microbit import *
import robotbit_library as r

# Define variables
pumpPin = 0x1
dispenseTime = 10*1000

def waterPlant():
    r.motor(pumpPin, 100)
    
    sleep(dispenseTime)
    
    r.motor_stop(pumpPin)
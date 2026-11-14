from microbit import *
import robotbit_library as r

# Define variables
pumpPin = 0x1
dispenseTime = 3000

def waterPlant():
    r.motor(pumpPin)
    
    sleep(dispenseTime)
    
    r.motor_stop(pumpPin)
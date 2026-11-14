from microbit import *
PWR = pin0
SENSE = pin1

def getMoisture(samples=1):
    PWR.write_digital(1)
    sleep(75)  
    total = 0
    for a in range(samples):
        total += SENSE.read_analog()
        sleep(5)
    PWR.write_digital(0)
    return total

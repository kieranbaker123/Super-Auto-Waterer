from microbit import *

# Define variables
pumpPin = pin1         
dispenseTime = 3000

while True:
    if moistureLevel < 500:
        display.show("W")  # Show 'W' for watering
        
        # Turn the water pump ON
        pumpPin.write_digital(1)
        
        sleep(dispenseTime)
        
        # Turn off the motor
        pumpPin.write_digital(0)

        
    sleep(3600000)  # Check every second
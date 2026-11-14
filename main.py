# -*- coding: utf-8 -*-

from waterPump import *
from temp import *
from display import *
from moisture import *
from microbit import *
import robotbit_library as r
import power

MOISTURE_THRESHOLD = 300
CHECK_INTERVAL_MS = 3*60*60*1000 # 3 hours

def main():
    while True:
        moisture = getMoisture()
        temp = getTemperature()
        
        if button_a.is_pressed() or button_b.is_pressed:
            flashTempMoisture(temp, moisture)
            sleep(5000) # ensure time betwen this message and a watering message
        
        if moisture < MOISTURE_THRESHOLD:
            flashWatering()
            waterPlant()
            sleep(5000) # leave message on screen for a bit
            
        clearDisplay()
        
        power.deep_sleep(
            wake_on=(button_a, button_b),
            ms=CHECK_INTERVAL_MS,
            run_every=True
        )

if __name__ == "__main__":
    main()
    

from microbit import *
from mb_lcd import LCD


lcd = LCD()
def flashTempMoisture(temperature, moistureLevel):
    lcd.write_word('It is currently {}°F The current moisture level is {}'.format(temperature, moistureLevel))

def flashWaterCycle(time):
    lcd.write_word('It has been {} since the last watering cycle'.format(time))

def flashWatering():
    lcd.write_word('The device is currently watering')

def clearDisplay():
    lcd.clear()

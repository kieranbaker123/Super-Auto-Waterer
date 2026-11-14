
from microbit import *
from mb_lcd import LCD


lcd = LCD()
def flashTempMoisture(temperature, moistureLevel):
    lcd.write_word(f'It is currently {temperature}° The current moisture level is {moistureLevel}')

def flashWaterCycle(time):
    lcd.write_word(f'IT has been {time} since the last watering cycle')

def flashWatering():
    lcd.write_word('The device is currently watering')

def clearDisplay():
    lcd.clear()

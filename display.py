
from microbit import *
from mb_lcd import LCD


lcd = LCD()
def flashTempMoisture(temperature, moistureLevel):
    lcd.write(0,0,'Temp {:.2f}{}C'.format(temperature, chr(223)))
    lcd.write(0,1,'Moisture: {}'.format(moistureLevel))
    
def flashWatering():
    lcd.write(0,0,'Watering...')

def clearDisplay():
    lcd.clear()

#src - https://toptechboy.com/lcd1602-display-library-for-micropython-and-the-raspberry-pi-pico-w/
#
# Adapted by: S Brophy
# Date: 10/23/23
# Revised the code from the original to use the i2c.write features of the microbit.  
#   Major changes occurred with the addressing and the address scan.  
#   Over all the other changes to the not use the buss worked fine from the original.
#
# NOTE:  Must use Vcc = 5 VDC
#        Had to change the freq which may cause problem with the other build in accelerometer and magnitometer
#

import microbit

import time
PCF85741 = 0x27
class LCD():
    def __init__(self, blen=1):
        microbit.i2c.init(freq=400000, sda=microbit.pin20, scl=microbit.pin19)
#        sda = microbit.pin20
#        scl = microbit.pin19
#        self.bus = machine.I2C(1,sda=sda, scl=scl, freq=400000)
        #print(self.bus.scan())
#        self.addr = self.scanAddress(PCF85741)
        self.addr = PCF85741
        self.blen = blen
        self.send_command(0x33) # Must initialize to 8-line mode at first
        time.sleep(0.005)
        self.send_command(0x32) # Then initialize to 4-line mode
        time.sleep(0.005)
        self.send_command(0x28) # 2 Lines & 5*7 dots
        time.sleep(0.005)
        self.send_command(0x0C) # Enable display without cursor
        time.sleep(0.005)
        self.send_command(0x01) # Clear Screen
    #    self.bus.writeto(self.addr, bytearray([0x08]))
        microbit.i2c.write(self.addr,bytearray([0x08]))

    def scanAddress(self, addr):
    # this needs to be updated to use a converted values of the address to performa the test
    #   also the raise Exception will no work in micropython
        devices = microbit.i2c.scan()
        if len(devices) == 0:
            raise Exception("No LCD found")
        if addr is not None:
            if addr in devices:
                return addr
            else:
                print(devices)
                
#                raise Exception(f"LCD at 0x{addr:2X} not found")
        elif 0x27 in devices:
            return 0x27
        elif 0x3F in devices:
            return 0x3F
        else:
            raise Exception("No LCD found")

    def write_word(self, data):
        temp = data
        if self.blen == 1:
            temp |= 0x08
        else:
            temp &= 0xF7
 #       self.bus.writeto(self.addr, bytearray([temp]))
        microbit.i2c.write(self.addr, bytearray([temp]))
    
    def send_command(self, cmd):
        # Send bit7-4 firstly
        buf = cmd & 0xF0
        buf |= 0x04               # RS = 0, RW = 0, EN = 1
        self.write_word(buf)
        time.sleep(0.002)
        buf &= 0xFB               # Make EN = 0
        self.write_word(buf)

        # Send bit3-0 secondly
        buf = (cmd & 0x0F) << 4
        buf |= 0x04               # RS = 0, RW = 0, EN = 1
        self.write_word(buf)
        time.sleep(0.002)
        buf &= 0xFB               # Make EN = 0
        self.write_word(buf)
    
    def send_data(self, data):
        # Send bit7-4 firstly
        buf = data & 0xF0
        buf |= 0x05               # RS = 1, RW = 0, EN = 1
        self.write_word(buf)
        time.sleep(0.002)
        buf &= 0xFB               # Make EN = 0
        self.write_word(buf)

        # Send bit3-0 secondly
        buf = (data & 0x0F) << 4
        buf |= 0x05               # RS = 1, RW = 0, EN = 1
        self.write_word(buf)
        time.sleep(0.002)
        buf &= 0xFB               # Make EN = 0
        self.write_word(buf)
    
    def clear(self):
        self.send_command(0x01) # Clear Screen
        
    def openlight(self):  # Enable the backlight
#        self.bus.writeto(self.addr,bytearray([0x08]))
        microbit.i2c.write(self.addr,bytearray([0x08]))
        # self.bus.close()
    
    def write(self, x, y, str):
        if x < 0:
            x = 0
        if x > 15:
            x = 15
        if y < 0:
            y = 0
        if y > 1:
            y = 1

        # Move cursor
        addr = 0x80 + 0x40 * y + x
        self.send_command(addr)

        for chr in str:
            self.send_data(ord(chr))
    
    def message(self, text):
        #print("message: %s"%text)
        for char in text:
            if char == '\n':
                self.send_command(0xC0) # next line
            else:
                self.send_data(ord(char))
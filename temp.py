def getTemperature(addr=0x76):
    i2c.init(freq=100000, sda=pin20, scl=pin19)

    # Calibration constants
    i2c.write(addr, b'\x88', repeat=True)
    c = i2c.read(addr, 6)
    T1 = c[0] | (c[1] << 8)
    T2 = c[2] | (c[3] << 8)
    T3 = c[4] | (c[5] << 8)
    if T2 > 32767: T2 -= 65536
    if T3 > 32767: T3 -= 65536

    # Trigger one measurement (forced mode)
    i2c.write(addr, b'\xf4\x25')
    sleep(10)

    # Read raw temperature
    i2c.write(addr, b'\xfa', repeat=True)
    d = i2c.read(addr, 3)
    adc = (d[0] << 12) | (d[1] << 4) | (d[2] >> 4)

    # Datasheet formula
    var1 = (adc / 16384 - T1 / 1024) * T2
    var2 = ((adc / 131072 - T1 / 8192) ** 2) * T3
    return (var1 + var2) / 5120

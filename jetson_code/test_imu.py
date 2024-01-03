import adafruit_bno055
import board

i2c = board.I2C()

sensor = adafruit_bno055.BNO055_I2C(i2c, address=0x28)
print(sensor.temperature)
while True:
    print(sensor.euler)
print(sensor.gravity)

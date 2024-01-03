import time
import board
from adafruit_seesaw import seesaw, pwmout
import busio

print(f"{board.SCL} SCL-< SDA-> {board.SDA}")
print(board.__dir__())
i2c = busio.I2C(board.SCL_1, board.SDA_1)

from adafruit_bus_device.i2c_device import I2CDevice
device = I2CDevice(i2c, 0x57)

print("--------------test", i2c.scan())
# i2c = board.STEMMA_I2C() # For using the built-in STEMMA QT connector on a
ss = seesaw.Seesaw(i2c)
PWM_PIN = 1 # If desired, change to any valid PWM output!
led = pwmout.PWMOut(ss, PWM_PIN)
delay = 0.01
while True:
    # The API PWM range is 0 to 65535, but we increment by 256 since our
    # resolution is often only 8 bits underneath
    for cycle in range(0, 65535, 256): #
        led.duty_cycle = cycle
        time.sleep(delay)
    for cycle in range(65534, 0, -256):
        led.duty_cycle = cycle
        time.sleep(delay)

import time
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c)

pca.frequency = 60
led_channel = pca.channels[8]
led_channel.duty_cycle = 0xffff
time.sleep(3)
led_channel.duty_cycle = 0x0000
time.sleep(3)
pca.deinit()

# This simple test outputs a 50% duty cycle PWM single on the 0th channel. Connect an LED and
# resistor in series to the pin to visualize duty cycle changes and its impact on brightness.

from board import SCL, SDA
import busio
import time
# Import the PCA9685 module.
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo

# Create the I2C bus interface.
i2c_bus = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c_bus)

# Set the PWM frequency to 60hz.
pca.frequency = 450

# Set the PWM duty cycle for channel zero to 50%. duty_cycle is 16 bits to match other PWM objects
# but the PCA9685 will only actually give 12 bits of resolution.
pca.channels[0].duty_cycle = 0xFFFF

NUM_MOTORS = 6
thrusters = []
for i in range(NUM_MOTORS):
    thrusters.append(servo.Servo(pca.channels[8 + i], min_pulse=1100, max_pulse=1900))

for mcs in thrusters:
    mcs.angle = 90
time.sleep(1)
for mcs in thrusters:
    mcs.angle = 0
time.sleep(3)
for mcs in thrusters:
    mcs.angle = 90
pca.deinit()


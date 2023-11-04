import iio
import time
import sys
import signal

#
# Copyright (C) 2023 Indrek Kruusa <indrek.kruusa@gmail.com>
# ADC demo program for MangoPi MQ F133/D1s RISC-V development board
#

def ctrl_c_handler(signum, frame):
    print("")
    print("Bye")
    print("")
    exit(0)

signal.signal(signal.SIGINT, ctrl_c_handler)

print("GPADC demo")
print("Input pin is on P2 header, pin no 20")
print("ADC converts the voltage between 0 - 1.8V")
print("Raw digital value will be printed")
print("Lowest value is 0 when the input pin is connected to the ground (GND pin is no 22 on the same header)")
print("Highest value is 4096 (1.8V)")
print("There is a 100k pull-up resistor connected between 1.8V rail and GPADC input on the board")
print("Test: connect 10kOhm potentiometer between GND and input pin and you should get values between 0...366")
print("Press CTRL+C to quit...")

DEVICE_NAME = "sun20i-gpadc"
CHANNEL_ID = "voltage0"

ctx = iio.LocalContext()
ctrl = ctx.find_device(DEVICE_NAME)
channel = ctrl.find_channel(CHANNEL_ID)
while True:
    print(channel.attrs["raw"].value)
    time.sleep(1)

#!/usr/bin/env python3

from time import sleep
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_3
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.led import Leds
from ev3dev2.button import Button

tank = MoveTank(OUTPUT_A, OUTPUT_D)
color_sensor = ColorSensor(INPUT_3, mode='COL-REFLECT')
b = Button()

def calibrate():
    print("WHITE?????")
    while True: #czekanie na input
        if b.any():
            break
    y = color_sensor.reflected_light_intensity
    return y

umax = 100

x = calibrate()
print(x)

while True: #czekanie na input
    pass
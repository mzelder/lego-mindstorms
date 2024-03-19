#!/usr/bin/env python3

import time as t
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_3
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.led import Leds
from ev3dev2.button import Button

tank = MoveTank(OUTPUT_A, OUTPUT_D)
color_sensor = ColorSensor(INPUT_3, mode='COL-REFLECT')

def calibrate():
    b = Button()
    print("WHITE?????")
    while True: #czekanie na input
        if b.any():
            break
    white = color_sensor.reflected_light_intensity
    print("WHITE TAKEN")
    t.sleep(1)
    print("BLACK?????")
    while True: #czekanie na input
        if b.any():
            break
    black = color_sensor.reflected_light_intensity

    return (white + black) / 2



umax = 100
alfa = 50
r = calibrate()

while True: #czekanie na input
    y = color_sensor.reflected_light_intensity
    e = r - y
    if e >= 0:
        motor_angle = alfa
    else:
        motor_angle = -alfa
    tank.on_for_degrees(SpeedPercent(motor_angle), SpeedPercent(motor_angle), 0)

    

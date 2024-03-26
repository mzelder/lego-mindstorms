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
    print("BLACK TAKEN")
    t.sleep(1)

    return (white + black) / 2

# Parametry regulatora PID
Kp = 0.2
Ki = 0.01
Kd = 0.01
r = calibrate()  # Docelowa wartość odbicia światła

# Zmienne pomocnicze
integral = 0
last_e = 0

while True:
    # Odczyt wartości z czujnika
    y = color_sensor.reflected_light_intensity

    # Obliczanie błędu
    e = r - y

    # Obliczanie całki błędu
    integral += e

    # Obliczanie pochodnej błędu
    derivative = e - last_e

    # Obliczanie wyjścia regulatora PID
    output = Kp*e + Ki*integral + Kd*derivative
    base_speed = 10

    # Ustawianie prędkości silników
    speed = max(min(output, 100), -100)  # Ograniczenie wartości do zakresu [-100, 100]
    left_speed = base_speed - speed
    right_speed = base_speed + speed
    tank.on(SpeedPercent(left_speed), SpeedPercent(right_speed))

    # Zapamiętanie błędu do następnego cyklu
    last_e = e

    # Krótka pauza, aby zapobiec zbyt szybkiemu cyklowaniu
    t.sleep(0.1)
    

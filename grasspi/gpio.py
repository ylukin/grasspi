#! /usr/bin/env python

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def get_gpio_input(channel):
	input_value = GPIO.input(channel)
	print input_value

GPIO.add_event_detect(17, GPIO.RISING, callback=get_gpio_input, bouncetime=300)

while True:
	time.sleep(10)

#! /usr/bin/env python

import sys
sys.path.append("ads1x15/")
from Adafruit_ADS1x15 import *

adc = ADS1x15(ic=0x01)

def getSoilMoisture():
	""" Return soil moisture level percentage """
	volts = adc.readADCSingleEnded(0, 4096, 250) / 1000
	percent = volts * 100
	return "%.0f" % percent


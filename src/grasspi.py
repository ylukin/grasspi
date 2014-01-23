#! /usr/bin/env python

import sys
sys.path.append("wmr928/")
sys.path.append("wunderground/")
from config import Config
from wmr928 import *
from wunderground import *

config_file = file('config.cfg')
cfg = Config(config_file)

def getWeatherData(provider):

    weather_data = {}
    if provider == 'wmr928':
    	wp = WMR928(cfg.TTY)
    elif provider == 'wunderground':
    	wp = Wunderground(cfg.wunderground_api_key, cfg.my_zip_code)
    weather_data['CurrentRain'] = wp.getData("CurrentRain")
    weather_data['TotalRain'] = wp.getData("TotalRain")
    weather_data['Wind'] = wp.getData("Wind")
    print 'Current rain is ' + str(weather_data['CurrentRain'])
    print 'Total rain is ' + str(weather_data['TotalRain'])
    print 'Wind speed is ' + str(weather_data['Wind'])

def main():
    """ gather weather data"""
    getWeatherData(cfg.weather_provider)

if __name__ == "__main__":
    main()

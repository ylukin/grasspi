#! /usr/bin/env python

import sys
sys.path.append("wmr928/")
sys.path.append("wunderground/")
from config import Config
from wmr928 import *
from wunderground import *
from grasspi_db import *

config_file = file('config.cfg')
cfg = Config(config_file)

def getWeatherData(provider):

    weather_data = {}
    if provider == 'wmr928':
    	wp = WMR928(cfg.TTY)
    elif provider == 'wunderground':
    	wp = Wunderground(cfg.wunderground_api_key, cfg.my_zip_code)
    weather_data = wp.getData()
    print weather_data.keys()	

def main():
    """ gather weather data"""

    # check if database already exists, if not, then create it
    if not isSQLite3('grasspi.db'):
	grasspi_create_db()

    getWeatherData("wunderground")
    #getWeatherData(cfg.weather_provider)
    #weather_data = {'provider':'wmr928','date':'01-31-2014','time':'11:30','current_rain':15,'total_rain':25,
    #'current_wind_speed':10,'current_wind_direction':67,'current_humidity':43,'current_air_pressure':10,
    #'current_shortwave_rad':3,'current_atm_rad':2,'day_length':18,'elevation':1300}
    #grasspi_add_db(weather_data,'weatherdata')
    #grasspi_print_db('weatherdata')

if __name__ == "__main__":
    main()

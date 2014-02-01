#! /usr/bin/env python

import sys
import datetime
sys.path.append("wmr928/")
sys.path.append("wunderground/")
from config import Config
from wmr928 import *
from wunderground import *
from grasspi_db import *

config_file = file('config.cfg')
cfg = Config(config_file)

def initProvider(provider):
    """ Initialize provider class and return weather data from it """

    if provider == 'wmr928':
        wp = WMR928(cfg.TTY)
    elif provider == 'wunderground':
        wp = Wunderground(cfg.wunderground_api_key, cfg.my_zip_code)
    
    return wp.getData()

def getWeatherData(provider):
    """ Get weather data from all providers and concat into dictionary """

    weather_data = {}

    # iterate through provider list, initialize each one and get data from it
    for p in cfg.providers:
        for key in p.keys():
    		weather_data = dict(initProvider(p.get(key)).items() + weather_data.items())		

    # add today's date and time
    weather_data['date'] = str(datetime.date.today())
    weather_data['time'] = datetime.datetime.now().strftime('%H:%M')

    # check if any values are still missing and initialize them
    for p in cfg.provider_map:
	for key in p.keys():
		if key not in weather_data.keys():
			weather_data[key] = 0
    return weather_data	

def main():
    """ gather weather data and store it in DB """

    # check if database already exists, if not, then create it
    if not isSQLite3('grasspi.db'):
	grasspi_create_db()

    # get weather data from all providers and store in DB
    myWeatherData = getWeatherData("wunderground")
    grasspi_add_db(myWeatherData,'weatherdata')
    grasspi_print_db('weatherdata')

if __name__ == "__main__":
    main()

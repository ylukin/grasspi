#! /usr/bin/env python

import sys
import datetime
import grasspi
#from config import Config

#config_file = file('/etc/grasspi/config.cfg')
#cfg = Config(config_file)

def initProvider(provider):
    """ Initialize provider class and return weather data from it """

    if provider == 'wmr928':
        wp = grasspi.wmr928.WMR928(grasspi.grasspi_config.cfg.TTY)
    elif provider == 'wunderground':
        wp = grasspi.wunderground.Wunderground(grasspi.grasspi_config.cfg.wunderground_api_key, grasspi.grasspi_config.cfg.my_zip_code)
    
    return wp.getData()

def getWeatherData():
    """ Get weather data from all providers, temporarily store into dictionary,
	and return the dictionary """

    weather_data = {}

    # iterate through provider list, initialize each one and get data from it
    for p in grasspi.grasspi_config.cfg.providers:
        for key in p.keys():
    		weather_data = dict(initProvider(p.get(key)).items() + weather_data.items())		

    # add today's date and time
    weather_data['date'] = str(datetime.date.today())
    weather_data['time'] = datetime.datetime.now().strftime('%H:%M')

    # check if any values are still missing and initialize them
    for p in grasspi.grasspi_config.cfg.provider_map:
	for key in p.keys():
		if key not in weather_data.keys():
			weather_data[key] = 0
    return weather_data	

def main():
    """ gather weather data and store it in DB """

    # check if database already exists, if not, then create it
    if not grasspi.grasspi_db.isSQLite3(grasspi.grasspi_config.cfg.db_file):
	grasspi.grasspi_db.grasspi_create_db('weatherdata', grasspi.grasspi_config.cfg.weatherdata_schema)
	grasspi.grasspi_db.grasspi_create_db('wateringschedule', grasspi.grasspi_config.cfg.wateringschedule_schema)

    # get weather data from all providers and store in DB
    myWeatherData = getWeatherData()
    grasspi.grasspi_db.grasspi_add_db('weatherdata',myWeatherData)
    grasspi.grasspi_db.grasspi_print_db('weatherdata')

if __name__ == "__main__":
    main()

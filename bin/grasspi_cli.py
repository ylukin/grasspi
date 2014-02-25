#! /usr/bin/env python

import sys
import datetime
import grasspi

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

def schedule_zone(zonenumber):
    zonesched = grasspi.grasspi_db.grasspi_query_db('wateringschedule','zonenumber',str(zonenumber))
    start_hour = zonesched[0][1][0:2]
    start_minute = zonesched[0][1][3:5]
    duration = zonesched[0][2]
    startTime = datetime.datetime.now().replace(hour=int(start_hour), minute=int(start_minute), second=0)
    currentTime = datetime.datetime.now()
    if (currentTime - startTime) < datetime.timedelta (minutes = 6) and (currentTime > startTime):
	print "Scheduling zone " + str(zonenumber) + " for " + str(duration) + " minutes"

def main():
    """ gather weather data and store it in DB """

    # check if database already exists, if not, then create it
    if not grasspi.grasspi_db.isSQLite3(grasspi.grasspi_config.cfg.db_file):
	grasspi.grasspi_db.grasspi_create_db('weatherdata', grasspi.grasspi_config.cfg.weatherdata_schema)
	grasspi.grasspi_db.grasspi_create_db('wateringschedule', grasspi.grasspi_config.cfg.wateringschedule_schema)

    # get weather data from all providers and store in DB
    myWeatherData = getWeatherData()
    grasspi.grasspi_db.grasspi_add_db('weatherdata',myWeatherData)

    # check all zone schedules and run them if it's time to water
    for i in range(1,grasspi.grasspi_config.cfg.num_zones+1):
	schedule_zone(i)

if __name__ == "__main__":
    main()

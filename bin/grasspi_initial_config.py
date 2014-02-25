#! /usr/bin/env python

import sys
import re
from config import *
from grasspi import grasspi_config
from grasspi import grasspi_db

if __name__ == "__main__":
	# initialize the database
	if not grasspi_db.isSQLite3(grasspi_config.cfg.db_file):
		grasspi_db.grasspi_create_db('weatherdata', grasspi_config.cfg.weatherdata_schema)
		grasspi_db.grasspi_create_db('wateringschedule', grasspi_config.cfg.wateringschedule_schema)

	# prompt for zip code
	zip_code = raw_input("Enter your 5 digit zip code: ")
	if re.match('^[0-9]{5}$', zip_code):
		grasspi_config.addConfigParameter('my_zip_code', zip_code)
	else:
		print ""
		print "Error: zip code must be 5 digits"
		sys.exit()
	# prompt for wunderground api key
	wu_api_key = raw_input("Enter Weather Underground API Key: ")
	if re.match('^[\w-]+$', wu_api_key):
		grasspi_config.addConfigParameter('wunderground_api_key', wu_api_key)
	else:
		print ""
		print "Error: API Key can only be alphanumeric"
		sys.exit()
	# prompt for number of zones and their run time
	zones = {}
	num_zones = input("Enter number of zones [1-8]: ")
	if re.match('^[1-8]$', str(num_zones)):
	    grasspi_config.addConfigParameter('num_zones', num_zones)
	    for i in range(1,num_zones+1):
			zones['zonenumber'] = i
			run_time = raw_input("Enter zone " + str(i) + " run time in minutes [1-60]: ")
			if re.match('^[1-9]$', run_time) or re.match('^[1-6][0-9]$', run_time):
				zones['duration'] = run_time
			else:
				print ""
				print "Error: zone run time must be [1-60] minutes"
				break
			start_time = raw_input("Enter zone " + str(i) + " start time in [hh:mm]: ")
			if re.match('^[0-9][0-9][\:][0-9][0-9]$', start_time):
				zones['starttime'] = start_time
			else:
				print ""
                                print "Error: zone start time must be in [hh:mm] format"
                                break
			grasspi_db.grasspi_add_db('wateringschedule',zones)
	else:
		print ""
		print "Error: number of zones supported is [1-8]"

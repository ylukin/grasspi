#! /usr/bin/env python

import re
from config import *
from grasspi import grasspi_config

config_directory = '/etc/grasspi'
config_file = '/etc/grasspi/config.cfg'

if __name__ == "__main__":
	# prompt for zip code
	zip_code = raw_input("Enter your 5 digit zip code: ")
	if re.match('^[0-9]{5}$', zip_code):
		grasspi_config.addConfigParameter('my_zip_code', zip_code)
	else:
		print "Zip code must be 5 digits"
	# prompt for wunderground api key
	wu_api_key = raw_input("Enter Weather Underground API Key: ")
	if re.match('^[\w-]+$', wu_api_key):
		grasspi_config.addConfigParameter('wunderground_api_key', wu_api_key)
	else:
		print "API Key can only be alphanumeric"

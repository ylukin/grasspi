#! /usr/bin/env python

import urllib2 
import json 
import sys
from grasspi import grasspi_config

class Wunderground:
	
	def __init__(self, api_key, zip_code):
		self.api_key = api_key
		self.zip_code = zip_code

	def getData(self):
		weather_data = {}

		# grab json data and parse it
		f = urllib2.urlopen('http://api.wunderground.com/api/' + self.api_key + '/geolookup/conditions/q/' + self.zip_code + '.json') 
		json_string = f.read() 
		parsed_json = json.loads(json_string) 
		location = parsed_json['location']['city'] 
		weather_data['current_temp'] = parsed_json['current_observation']['temp_c'] 
		weather_data['current_humidity'] = parsed_json['current_observation']['relative_humidity']
		weather_data['current_rain'] = parsed_json['current_observation']['precip_1hr_in']
		weather_data['total_rain'] = parsed_json['current_observation']['precip_today_in']
		weather_data['current_wind_speed'] = parsed_json['current_observation']['wind_mph']	
		weather_data['current_wind_direction'] = parsed_json['current_observation']['wind_dir']
		weather_data['current_air_pressure'] = parsed_json['current_observation']['pressure_mb']
		weather_data['elevation'] = parsed_json['current_observation']['display_location']['elevation']
		f.close()

		# iterate through data-to-provider mappings in config file and remove any values
		#   that are not from this provider
		for p in grasspi_config.cfg.provider_map:
			for key in p.keys():
				if p.get(key) != "wunderground":
					weather_data.pop(key, None)

		return weather_data

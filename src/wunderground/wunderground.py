#! /usr/bin/env python

import urllib2 
import json 
import sys
from config import Config

config_file = file('config.cfg')
cfg = Config(config_file)


class Wunderground:
	
	def __init__(self, api_key, zip_code):
		self.api_key = api_key
		self.zip_code = zip_code

	def getData(self):
	
		weather_data = {}
		f = urllib2.urlopen('http://api.wunderground.com/api/' + self.api_key + '/geolookup/conditions/q/' + self.zip_code + '.json') 
		json_string = f.read() 
		parsed_json = json.loads(json_string) 
		location = parsed_json['location']['city'] 
		temp_f = parsed_json['current_observation']['temp_f'] 
		weather_data['current_humidity'] = parsed_json['current_observation']['relative_humidity']
		weather_data['current_rain'] = parsed_json['current_observation']['precip_1hr_in']
		weather_data['total_rain'] = parsed_json['current_observation']['precip_today_in']
		weather_data['current_wind_speed'] = parsed_json['current_observation']['wind_mph']	
		f.close()

		for p in cfg.providers:
			for key in p.keys():
				if p.get(key) != "wunderground":
					weather_data.pop(key, None)

		return weather_data

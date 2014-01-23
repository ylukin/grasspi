#! /usr/bin/env python

import urllib2 
import json 
import sys

class Wunderground:
	
	def __init__(self, api_key, zip_code):
		self.api_key = api_key
		self.zip_code = zip_code

	def getData(self, type):

		f = urllib2.urlopen('http://api.wunderground.com/api/' + self.api_key + '/geolookup/conditions/q/' + self.zip_code + '.json') 
		json_string = f.read() 
		parsed_json = json.loads(json_string) 
		location = parsed_json['location']['city'] 
		temp_f = parsed_json['current_observation']['temp_f'] 
		rh = parsed_json['current_observation']['relative_humidity']
		currentRain = parsed_json['current_observation']['precip_1hr_in']
		totalRain = parsed_json['current_observation']['precip_today_in']
		windspeed = parsed_json['current_observation']['wind_mph']	
		f.close()

		if type == 'CurrentRain':
			return currentRain
		elif type == 'TotalRain':
			return totalRain
		elif type == 'Wind':
			return windspeed

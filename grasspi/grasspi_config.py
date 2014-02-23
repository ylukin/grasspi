#! /usr/bin/env python

from config import *


config_file = file('/etc/grasspi/config.cfg')
cfg = Config(config_file)

def addConfigParameter(param_name, value):
	""" Add a new global parameter of type 'parameter : value' to config file, 
	overwrite existing value if it already exists """

	cfg.addMapping(param_name, value, None, True)
	f = file(config_file, 'w')
	cfg.save(f)

def delConfigParameter(param_name):
	""" Remove existing global parameter from config file """

	try:
		cfg.__delitem__(param_name)
		f = file(config_file, 'w')
		cfg.save(f)
	except AttributeError:
		print "Global parameter " + param_name + " not found in config file"

def addProvider(provider):
	""" Add a new provider to list of providers in config file """

	current_num_providers = len(cfg.providers)
	newProvider = Mapping()
	newProvider.addMapping('provider',provider,None,True)
	cfg.providers.append(newProvider,'')
	f = file(config_file, 'w')
	cfg.save(f)

def delProvider(provider):
	""" Remove existing provider from config file """

	for p in cfg.providers:
		for key in p.keys():
			if p.get(key) == provider:
				p.__delitem__('provider')
	f = file(config_file, 'w')
	cfg.save(f)

def modifyProviderMapping(param_name, provider):
	""" Modify provider for existing data value in config file """

	if param_name == "current_rain":
		cfg.provider_map[0].current_rain = provider
	elif param_name == "total_rain":
		cfg.provider_map[1].total_rain = provider
	elif param_name == "current_temp":
                cfg.provider_map[2].current_temp = provider
	elif param_name == "current_wind_speed":
                cfg.provider_map[3].current_wind_speed = provider
	elif param_name == "current_wind_direction":
                cfg.provider_map[4].current_wind_direction = provider
	elif param_name == "current_humidity":
                cfg.provider_map[5].current_humidity = provider
	elif param_name == "current_air_pressure":
                cfg.provider_map[6].current_air_pressure = provider
	elif param_name == "current_shortwave_rad":
                cfg.provider_map[7].current_shortwave_rad = provider
	elif param_name == "total_atm_rad":
                cfg.provider_map[8].current_atm_rad = provider
	elif param_name == "day_length":
                cfg.provider_map[9].day_length = provider
	elif param_name == "elevation":
                cfg.provider_map[10].elevation = provider

	f = file(config_file, 'w')
        cfg.save(f)
	


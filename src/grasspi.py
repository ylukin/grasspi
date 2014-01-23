#! /usr/bin/env python

import sys
sys.path.append("wmr928/")
from wmr928 import *

def main():
    """ gather weather data"""

    weather_data = {}
    ws = WMR928()
    weather_data['CurrentRain'] = ws.getData("CurrentRain")
    weather_data['TotalRain'] = ws.getData("TotalRain")
    weather_data['Wind'] = ws.getData("Wind")
    print 'Current rain is ' + str(weather_data['CurrentRain'])
    print 'Total rain is ' + str(weather_data['TotalRain'])
    print 'Wind sped is ' + str(weather_data['Wind'])

if __name__ == "__main__":
    main()

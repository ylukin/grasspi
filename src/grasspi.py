#! /usr/bin/env python

import sys
sys.path.append("wmr928/")
from wmr928 import *

grabOneReading = False

dataType = {"wind": 0,
	"rain": 1,
	"thermohygro": 2,
	"mushroom": 3,
	"thermo": 4,
	"thermohygrobaro": 5,
	"indoorthermohygrobaro": 6,
	"all": 999}
	

def main():
    """ gather data"""

    global grabOneReading
    # check if user requested data from specific sensor
    if len(sys.argv) > 1:
	grabOneReading = True
	key = sys.argv[1]
    else:
	key = "all"

    dec = WMR928()
    if grabOneReading:
	while dec.notFound:
        	dec.getStart()
        	dec.decode(dataType[key])
    else:
	while True:
		dec.getStart()
		dec.decode(key)

if __name__ == "__main__":
    main()

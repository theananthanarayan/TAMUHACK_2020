import string, sys, random, datetime, json
import requests
import numpy as np

def ReadJSONFile(inFile):
    lines = inFile.readlines()
    flightsJSON = []
    for line in lines:
        flightData = json.loads(line)
        flightsJSON.append(flightData)

    return flightsJSON

class FlightsDatabase:
    def __init__(self, flightsJSON):
	    self.flightsJSON = flightsJSON

    def search(self, attr, key):
        results = []
        for flightData in self.flightsJSON:
            if(flightData[attr] == key):
                results.append(flightData)
        return results

    def findFirstAirportDestination(self, flightNumber):
        results = self.search("marketingFlightNumber", flightNumber)
        if len(results) > 0:
            return results[0]["destinationAirportCode"]
        else:
            return None

if len(sys.argv) < 2:
    raise Exception("Not enough input arguments")
	
inFile = open("SouthwestFlights.json", "rt")
flightNumber = sys.argv[1]

flightsJSON = ReadJSONFile(inFile)

fdb = FlightsDatabase(flightsJSON)

print(fdb.findFirstAirportDestination(flightNumber))


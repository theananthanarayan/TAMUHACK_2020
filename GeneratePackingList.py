import string, sys, random, datetime, json
import numpy as np

def ReadJSONFile(inFile):
    lines = inFile.readlines()
    jsonData = []
    for line in lines:
        jsonObject = json.loads(line)
        jsonData.append(jsonObject)

    return jsonData
	
def ConvertStringToDateTime(stringDate):
    dateTimeVal = datetime.strptime(stringDate, "%Y-%m-%dT%H-%M%S")

if len(sys.argv) < 2:
    raise Exception("Not enough input arguments")
	
inFile = open(sys.argv[1], "rt")

jsonData = ReadJSONFile(inFile)

print(jsonData)
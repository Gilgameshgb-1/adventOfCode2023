#Read data
from pickle import FALSE, TRUE
from xml.etree.ElementTree import tostring
import re

file_path = 'data.txt'  
with open(file_path, 'r') as file:
    data = file.readlines()

data = [line.strip() for line in data]

gameNo = 1

requirements = [12, 13, 14] #red, green, blue

def checkValidity(list):
    hashMap = {}
    list = list.split(',')
    for i in range(0, len(list)):
        if 'red' in list[i]:
            matchRed = re.search(r'\b(\d+)\b', list[i])
            hashMap['red'] = int(matchRed.group(1))
        if 'green' in list[i]:
            matchGreen = re.search(r'\b(\d+)\b', list[i])
            hashMap['green'] = int(matchGreen.group(1))
        if 'blue' in list[i]:
            matchBlue = re.search(r'\b(\d+)\b', list[i])
            hashMap['blue'] = int(matchBlue.group(1))
    return hashMap

arrOfPwrs = []

for strParse in data:
    countValid = 0
    arrOfHashMaps = []
    tmpStr = 'Game ' + str(gameNo) + ': '
    strParse = strParse.replace(tmpStr, '')
    parsedData = strParse.split(';')
    for i in range (0, len(parsedData)):
        tmpHashMap = checkValidity(parsedData[i])
        arrOfHashMaps.append(tmpHashMap)
    arrOfReds = []
    arrOfGreens = []
    arrOfBlues = []
    for i in range(0, len(arrOfHashMaps)):
        if 'red' in arrOfHashMaps[i]:
            arrOfReds.append(arrOfHashMaps[i]['red'])
        if 'green' in arrOfHashMaps[i]:
            arrOfGreens.append(arrOfHashMaps[i]['green'])
        if 'blue' in arrOfHashMaps[i]:
            arrOfBlues.append(arrOfHashMaps[i]['blue'])
    arrOfPwrs.append(max(arrOfReds)*max(arrOfGreens)*max(arrOfBlues))
    gameNo = gameNo+1

print(sum(arrOfPwrs))

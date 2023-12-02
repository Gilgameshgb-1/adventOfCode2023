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
    list = list.split(',')
    for i in range(0, len(list)):
        #print(list[i])
        if 'red' in list[i]:
            matchRed = re.search(r'\b(\d+)\b', list[i])
            #print('red ', 'req: ', requirements[0], ' match: ', matchRed.group(1))
            if(requirements[0] < int(matchRed.group(1))):
                #print("!R")
                return FALSE
        if 'green' in list[i]:
            matchGreen = re.search(r'\b(\d+)\b', list[i])
            #print('green ', 'req: ', requirements[1], ' match: ', matchGreen.group(1))
            if(requirements[1] < int(matchGreen.group(1))):
                #print("!G")
                return FALSE
        if 'blue' in list[i]:
            matchBlue = re.search(r'\b(\d+)\b', list[i])
            #print(list[i])
            #print('blue ','req: ', requirements[2], ' match: ', matchBlue.group(1))
            if(requirements[2] < int(matchBlue.group(1))):
                #print("!B")
                return FALSE
    return TRUE

sum = 0

for strParse in data:
    countValid = 0
    tmpStr = 'Game ' + str(gameNo) + ': '
    strParse = strParse.replace(tmpStr, '')
    parsedData = strParse.split(';')
    #print(parsedData)
    #print(len(parsedData))
    for i in range (0, len(parsedData)):
        if checkValidity(parsedData[i]) == TRUE:
            countValid = countValid + 1
    #print("valid: ", countValid)
    #print("parsedDataLen", len(parsedData))
    #print("-==-=-=-=-=-=-=-=-=-=-=-")
    if countValid == len(parsedData):
        #print("Valid game number: ",gameNo)
        sum = sum + gameNo
    gameNo = gameNo+1

print(sum)

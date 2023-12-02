import re
#Read data
file_path = 'data.txt'  
with open(file_path, 'r') as file:
    data = file.readlines()

data = [line.strip() for line in data]

arrOfNums = []

def convertNumbersALittle(str): #This regex could probably be simplified
    str = str.upper()
    str = re.sub(r'ONE', 'O1E', str)
    str = re.sub(r'TWO', 'T2O', str)
    str = re.sub(r'THREE', 'T3E', str)
    str = re.sub(r'FOUR', 'F4R', str)
    str = re.sub(r'FIVE', 'F5E', str)
    str = re.sub(r'SIX', 'S6X', str)
    str = re.sub(r'SEVEN', 'S7N', str)
    str = re.sub(r'EIGHT', 'E8T', str)
    str = re.sub(r'NINE', 'N9E', str)
    return str


for str in data:
    str = convertNumbersALittle(str)
    firstNumber = ''
    secondNumber = ''
    length = len(str)
    for i in range(0, length):
        if(str[i].isdigit()):
            firstNumber = str[i]
            break
    for i in range(length-1, -1, -1):
        if(str[i].isdigit()):
            secondNumber = str[i]
            break
    arrOfNums.append(firstNumber+secondNumber)

sum = 0

for el in arrOfNums:
    sum = sum + int(el)
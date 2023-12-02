#Read data
file_path = 'data.txt'  
with open(file_path, 'r') as file:
    data = file.readlines()

data = [line.strip() for line in data]

arrOfNums = []

for str in data:
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

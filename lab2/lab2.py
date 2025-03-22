import re
from string import ascii_lowercase  
from itertools import count


#Задание a

text = "(24444+3124)*4"
pattern = "\d+"
replacement = "x"
result = re.sub(pattern, replacement, text)
print("Задание a:", result)

#Задание b

text = "(2+3.1123)*4.2"
pattern = "\d+\.?\d*"
replacement = "x"
result = re.sub(pattern, replacement, text)
print("Задание b:", result)

#Задание c


def replaceNumbers(text):
    letter = {}
    counterLetters = 0

    def replacement_callback(match):
        nonlocal counterLetters
        number = match.group(0) 
        if number not in letter:
            letter[number] = ascii_lowercase[counterLetters]
            counterLetters += 1
        return letter[number]  

    pattern = "\d+\.?\d*"
    result = re.sub(pattern, replacement_callback, text)
    return result

text = "2+(2+4.2)+3-3/11"
result = replaceNumbers(text)
print("Задание c:", result)

#Задание d

text = "4(2+3)*4"
pattern = "\d+(?!\()" #Негативный просмотр вперёд
replacement = "x"
result = re.sub(pattern, replacement, text)
print("Задание d:", result)

#Задание e

text = "(2+334)*41/1*2424"
pattern = "\d{2,}"
replacement = "x"
result = re.sub(pattern, replacement, text)
print("Задание e:", result)

#Задание f
text = "(2+3)*4 + 2*2 - 11*424"
pattern = "\*\d+"
counter = count()
result = re.sub(pattern, lambda match: ascii_lowercase[next(counter)] , text)
print("Задание f:", result)

#Задание g

text = "2*3+4-1"
pattern = "\d+"
text = re.sub(pattern, lambda match: ascii_lowercase[next(counter)] , text)
print("Промежуточное g:", text)
pattern = "[+/*-][a-z]"
matches = re.finditer(pattern, text)
counterg = count()
replaceText = {}
for match in matches:
    replaceText[next(counterg)] = match.group(0)[1:] + match.group(0)[0]
counterg = count()
result = re.sub(pattern, replaceText[next(counterg)], text)
print("Задание g:", result)


import re


text = "Сегодня 31-05-2023, а завтра будет 01-06-2023."
pattern = r"([0-3]?[0-9]-(0[1-9]|1[0-2])-[0-9]{4})"
match = re.findall(pattern, text)
if match:
    print("Даты: ",match)
else:
    print("Дат не найдено.")


    
    #print("Даты:", match.group())
import re
text = "Сегодня 31-05-2023, а завтра будет 01-06-2023"
pattern1 = r"\d{2}-\d{2}-\d{4}"  
match = re.findall(pattern1, text)
if match:
 print("Найдены даты:", match)
else:
 print("Даты не найдены.")


pattern2 = r"(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}"
matches = re.finditer(pattern2, text)
for match in matches:
    print("Дата:", match.group(0))  
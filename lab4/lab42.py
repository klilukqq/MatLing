from textblob import TextBlob

input_file = 'lab4/lab4InputEn'  
output_file = 'lab4/lab4Output'  



with open(input_file, 'r', encoding='utf-8') as file:
    text = file.read()


blob = TextBlob(text)
tokens = blob.words


with open(output_file, 'w', encoding='utf-8') as file:
    file.write('\n'.join(tokens))

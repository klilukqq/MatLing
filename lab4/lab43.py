import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

input_file = 'lab4/lab4InputEn'  
output_file = 'lab4/lab4Output'  



with open(input_file, 'r') as file:
    text = file.read()


tokens = word_tokenize(text)


with open(output_file, 'w', encoding='utf-8') as file:
    file.write('\n'.join(tokens))


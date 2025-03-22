import spacy

nlp = spacy.load('en_core_web_sm')
input_file = 'lab4/lab4InputEn'  

#nlp = spacy.load('ru_core_news_sm') #Для русского языка
#input_file = 'lab4/lab4InputRu' 

output_file = 'lab4/lab4Output'  

with open(input_file, 'r', encoding='utf-8') as file:
    text = file.read()

doc = nlp(text)
token_info = doc
'''
token_info = [
    f"Token: {token.text}, Lemma: {token.lemma_}, POS: {token.pos_}"
    for token in doc
]'''

with open(output_file, 'w', encoding='utf-8') as file:
    file.write('\n'.join(token_info))

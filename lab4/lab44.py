import tensorflow as tf
import tensorflow_text as tf_text

input_file = 'lab4/lab4InputEn'  
output_file = 'lab4/lab4Output'  



with open(input_file, 'r') as file:
    text = file.read()


tokenizer = tf_text.WhitespaceTokenizer()
tokens = tokenizer.tokenize(text)
tokens = tokens.to_list()


with open(output_file, 'w', encoding='utf-8') as file:
    file.write('\n'.join(tokens))

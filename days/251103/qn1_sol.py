words_seq = input('Words (separated by space):')
print(words_seq)
words = words_seq.split() #' '
print(words, type(words))
words_tuple = tuple(words)
print(words_tuple, type(words_tuple))

'''
output_file = open('qn01_data.txt', 'w')
output_file.write(f'list:{words}')
output_file.write(f'tuple:{words_tuple}')
output_file.close()
'''

with open('qn01_data.txt', 'w') as output_file:
    output_file.write(f'list:{words}\n')
    output_file.write(f'tuple:{words_tuple}\n')

with open('qn01_data.txt', 'r') as input_file:
    file_words_list_line = input_file.readline()
    file_words_tuple_line =  input_file.readline()
    print(file_words_list_line)
    print(file_words_tuple_line)
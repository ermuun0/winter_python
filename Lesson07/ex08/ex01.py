fhand = open('words.txt')
words_dict = dict()
for line in fhand:
    line = line.rstrip()
    word_list=line.split(' ')
    
    for word in word_list:    
        if word not in words_dict:
            words_dict[word] = '1'
print(words_dict)
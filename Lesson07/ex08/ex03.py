fhand = open('mbox-short.txt')
word_dict = dict()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From'):
         word_line = line.split()
         print(word_line)
         gmail = word_line[1]
         word_dict[gmail] = word_dict.get(gmail, 0)+1
print(word_dict)
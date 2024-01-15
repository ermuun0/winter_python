fhand = open('mbox-short.txt')
word_dict = dict()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From'):
         word_line = line.split()
         print (word_line)
         if len(word_line)>= 3:
             day = word_line[2]
             word_dict[day] =word_dict.get(day, 0)+1
print(word_dict)
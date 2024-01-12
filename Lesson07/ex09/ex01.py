fhand = open('mbox-short.txt')
word_dict = dict()
numbers = []
for line in fhand:
    line = line.rstrip()
    if line.startswith('From'):
        word_list=line.split(' ')
        print (word_list)
        gmail = word_list[1]
        word_dict[gmail] = word_dict.get(gmail, 0)+1
print(word_dict)

max = 0
for word in word_dict.items():
    print(word)
    email , count = word 
    print(count)
    numbers.append(count)
    for number in numbers:
        if max < number:
            max = number
            
print(max)